<template>
    <div>
      <h2>Tiempo en Bucle</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Tiempo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="usuario in usuarios" :key="usuario.id">
            <td>{{ usuario.nombre }}</td>
            <td>{{ usuario.tiempo }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        usuarios: [
          { id: 1, nombre: 'Usuario 1', tiempo: '00:00:00' },
          { id: 2, nombre: 'Usuario 2', tiempo: '00:00:00' },
          { id: 3, nombre: 'Usuario 3', tiempo: '00:00:00' },
        ],
        tiempoIntervalo: null
      };
    },
    mounted() {
      this.tiempoIntervalo = setInterval(() => {
        this.actualizarTiempo();
      }, 1000);
    },
    beforeUnmount() {
      clearInterval(this.tiempoIntervalo);
    },
    methods: {
      actualizarTiempo() {
        const ahora = new Date();
        this.usuarios.forEach((usuario) => {
          usuario.tiempo = this.formatearTiempo(ahora);
        });
      },
      formatearTiempo(tiempo) {
        const horas = tiempo.getHours().toString().padStart(2, '0');
        const minutos = tiempo.getMinutes().toString().padStart(2, '0');
        const segundos = tiempo.getSeconds().toString().padStart(2, '0');
        return `${horas}:${minutos}:${segundos}`;
      }
    }
  };
  </script>
  