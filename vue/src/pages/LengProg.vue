<template>
    <div class="row py-2">
    <div class="offset-md-2 col-md-7">
        <h2>Lenguajes de programacion</h2>
        <ul>
        <div v-for="len in arrayLenguajes" :key="len.id">
            <li v-text="len.nombre+', '+len.anio"></li>
        </div>
    </ul>
    </div>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                compatConfig: { MODE: 3 },
                arrayLenguajes: []
            }
        },
        methods:{
           listarLenguajes(){
            let me = this;
                this.$axios.get('http://localhost:8000/api/v1/lenguajes/?format=json')
                .then(function(response){
                    me.arrayLenguajes = response.data
                })
           }
        },
        mounted(){
            this.listarLenguajes()
        }
    }
</script>