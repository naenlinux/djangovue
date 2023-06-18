<template>
    <div class="row">
        <div class="offset-md-2 col-md-8">
            <h2>Pedidos: <button class="btn btn-primary btn-sm" @click="modalOpen()">Nuevo +</button></h2>
            <table class="table table-bordered table-striped">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Pedido</th>
                        <th>Direccion de entrega</th>
                        <th>Hora</th>
                        <th>Tiempo del pedido</th>
                        <th>Opcion</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(ped, index) in arrayPedido" :key="ped.id">
                        <td>{{ index+1 }}</td>
                        <td>{{ ped.nombre }}</td>
                        <td>{{ ped.direccion }}</td>
                        <td>{{ ped.hora.substr(0,8) }}</td>
                        <td>{{ ped.tiempo }}</td>
                        <td><button class="btn btn-sm btn-danger" @click="eliminarPedido(ped.id)">Eliminar</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <!--- MODAL PEDIDO --->
        <div v-if="showModal">
            <div class="modal">
                <div class="modal-overlay"></div>
                <div class="modal-content">
                    <div class="modal-header bg-info text-white">
                        <h4>Agregar nuevo pedido</h4>
                        <button type="button" class="btn-close" @click="cerrarModal()"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3 row">
                            <label for="" class="col-sm-3 col-form-label">Pedido:</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" v-model="nombre">
                            </div>
                        </div>
                        <div class="mb-3 row">
                            <label for="" class="col-sm-3 col-form-label">Direccion:</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" v-model="direccion">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" @click="cerrarModal()">Cerrar</button>
                        <button type="button" class="btn btn-primary" @click="registrarPedido()">GUARDAR</button>
                    </div>
                </div>
            </div>
        </div>
    <!--- FIN MODAL PEDIDO --->
</template>
<script>
    export default{
        data(){
            return{
                nombre:'',
                direccion:'',
                showModal: false,
                arrayPedido:[],
                tiempoIntervalo: null,
            }
        },
        methods:{
            listarPedidos(){
                let me = this
                this.$axios.get('http://localhost:8000/api/v1/nuevopedido/?format=json')
                .then(function (response) {
                  me.arrayPedido = response.data
                })
                .catch(function (error) {
                    console.log(error);
                })
            },
            registrarPedido(){
                let me = this
                this.$axios.post('http://localhost:8000/api/v1/nuevopedido/', {
                    nombre: me.nombre,
                    direccion: me.direccion,
                })
                .then(function (response) {
                    me.listarPedidos()
                    me.nombre =''
                    me.direccion = ''
                    me.cerrarModal()
                    console.log(response);
                })
            },
            eliminarPedido(id){
                let me = this
                this.$swal.fire({
                    title: 'Eliminar registro',
                    text: 'Presione si para eliminar',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, eliminar'
                }).then((result)=>{
                    if(result.isConfirmed){
                        this.$axios.put('http://localhost:8000/api/v1/nuevopedido/'+id+'/',{
                            es_activo : 0
                        })
                        .then(()=>{
                            me.cerrarModal()
                            me.listarPedidos()
                        })
                    }
                })
            },
            modalOpen(){
                this.showModal = true
            },
            cerrarModal(){
                this.showModal = false
            },
            actualizarTiempo() {
                const ahora = new Date();
                this.arrayPedido.forEach((usuario) => {
                    //restar hora del registro con la hora actual
                    let resta = ahora - new Date(`1970-01-01T${usuario.hora}Z`)
                    const diferenciaTiempo = new Date(resta)
                    usuario.tiempo = this.formatearTiempo(diferenciaTiempo);
                });
            },
            formatearTiempo(tiempo) {
                const horas = tiempo.getHours().toString().padStart(2, '0');
                const minutos = tiempo.getMinutes().toString().padStart(2, '0');
                const segundos = tiempo.getSeconds().toString().padStart(2, '0');
                return `${horas}:${minutos}:${segundos}`;
            }
        },
        beforeUnmount() {
            clearInterval(this.tiempoIntervalo);
        },
        mounted(){
            this.listarPedidos()

            this.tiempoIntervalo = setInterval(() => {
                this.actualizarTiempo();
            }, 1000);
        }
    }
</script>
<style scoped>
    .modal{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    .modal-overlay{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
    }
    .modal-content{
        width: 40%;
        background-color: white;
        margin-top: 100px;
    }
</style>