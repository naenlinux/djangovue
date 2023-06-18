<template>
    <div class="row py-2">
    <div class="offset-md-2 col-md-3">
        <h2>Registrar nuevo</h2>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Nombre" v-model="nombre">
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Nickname" v-model="nickname">
        </div>
        <div class="mb-3">
            <input type="number" class="form-control" placeholder="Edad" v-model="edad">
        </div>
        <div class="d-grid gap-2">
            <button class="btn btn-primary btn-block" @click="registrarProgramador()">GUARDAR</button>
        </div><!--- MODAL PEDIDO --->
        <div class="mt-3">
            <div v-for="err in array_error" :key="err">
                <p class="text-danger">* {{ err }}</p>
            </div>
        </div>
    </div>
    <div class="offset-md-1 col-md-4">    
    <h2>Programadores</h2>
    <table class="table table-sm table-bordered table-striped">
        <thead>
            <tr>
                <th>#</th>
                <th>Nombres</th>
                <th>Nickname</th>
                <th>Edad</th>
                <th colspan="2">Opciones</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="( p,index ) in programadores" :key="p.id">
                <td>{{ index+1 }}</td>
                <td v-text="p.nombre"></td>
                <td v-text="p.nickname"></td>
                <td>{{ p.edad }}</td>
                <td>
                    <button class="btn btn-sm btn-warning" @click="modalEditar(p.id,p.nombre,p.nickname,p.edad)">Editar</button>
                </td>
                <td>
                    <button class="btn btn-sm btn-danger" @click="elminarRegistro(p.id,p.nombre)">Eliminar</button>
                </td>
            </tr>
        </tbody>
    </table>
    </div>
</div>
    <div v-if="showModal">
        <div class="modal" >
            <div class="modal-overlay"></div>
            <div class="modal-content">
                <div class="modal-header bg-info text-white">
                    <h4 class="modal-title">Editar registro</h4>
                    <button type="button" class="btn-close" @click="cerrarModal()"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3 row">
                        <label class="col-sm-3 col-form-label">Nombre:</label>
                        <div class="col-sm-9">
                        <input type="text" class="form-control" v-model="nombreupdate">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label class="col-sm-3 col-form-label">Nickname:</label>
                        <div class="col-sm-9">
                        <input type="text" class="form-control" v-model="nicknameupdate">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label class="col-sm-3 col-form-label">Edad:</label>
                        <div class="col-sm-9">
                        <input type="number" class="form-control" v-model="edadupdate">
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="cerrarModal">Cerrar</button>
                    <button type="button" class="btn btn-primary" @click="updateRegistro()">GUARDAR</button>
                </div>
            </div>
        </div>
    </div>
  
</template>
<script>
    export default{
        data(){
            return {
                programadores:[],
                nombre: '',
                nickname:'',
                edad:'',
                nombreupdate: '',
                nicknameupdate:'',
                edadupdate:'',
                showModal : false,
                id:'',
                es_activo:'',
                array_error :[],
            }
        },
        methods:{
            listarProgramadores(){
                let me = this;
                this.$axios.get('http://localhost:8000/api/v1/programadores/?format=json')
                .then(function(response){
                    me.programadores = response.data
                })
            },
            validar_registro(){
                this.array_error = []
                if(this.nombre == ''){
                    this.array_error.push('El nombre no debe estar vacio')
                }
                if(this.nickname == ''){
                    this.array_error.push('El nickname no debe estar vacio')
                }
                if(this.edad == ''){
                    this.array_error.push('La edad no debe estar vacio')
                }
                if(this.array_error.length > 0){
                    return 1
                }else{
                    return 0
                }
            },
            registrarProgramador(){
                let me = this

                if(this.validar_registro()){
                    return                   
                }
                this.$axios.post('http://localhost:8000/api/v1/programadores/',{
                    nombre : me.nombre,
                    nickname : me.nickname,
                    edad : me.edad
                })
                .then(function(response){
                    console.log(response)
                    me.listarProgramadores()
                    me.nombre = ''
                    me.nickname = ''
                    me.edad = ''
                })            
                
            },
            modalEditar(id,nombre,nickname,edad){
                this.id = id,
                this.nombreupdate = nombre
                this.nicknameupdate = nickname
                this.edadupdate = edad
                this.showModal = true

            },
            updateRegistro(){
                let me = this
                this.$axios.put('http://localhost:8000/api/v1/programadores/'+me.id+'/',{
                    nombre : me.nombreupdate,
                    nickname : me.nicknameupdate,
                    edad : me.edadupdate
                })
                .then(function(response){
                    console.log(response)
                    me.listarProgramadores()
                    me.cerrarModal()
                })
            },
            cerrarModal(){
                this.showModal=false
                this.id = ''
                this.nombreupdate = ''
                this.nicknameupdate = ''
                this.edadupdate = ''
            },
            elminarRegistro(id,nombre){
                let me = this
                this.$swal.fire({
                title: 'Eliminar a: \n'+nombre,
                text: 'Presione si para eliminar',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, eliminar'
                }).then((result) => {
                if (result.isConfirmed) {
                    this.$axios.put('http://localhost:8000/api/v1/programadores/'+id+'/',{
                        es_activo : 0,
                    })
                    .then(function(response){
                        console.log(response)
                        me.listarProgramadores()
                        me.cerrarModal()
                    })
                }
                })
            }
        },
        mounted(){
            this.listarProgramadores()
        }
    }
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center ;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  width: 40%;
  background-color: white;
  
  /*border-radius: 4px;*/
  margin-top: 100px;
}
</style>
