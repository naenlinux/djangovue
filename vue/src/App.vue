<template>
      <div class="row py-4">
        <div class="offset-md-2 col-md-8">
          <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
            <ul class="nav">
            <li class="nav-item">
              <router-link :to="{ name: 'programadores' }" class="nav-link">Programadores</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'lenguajes' }" class="nav-link">Lenguajes</router-link>
            </li>
            <li class="nav-item">
                <router-link :to="{ name: 'pedido' }" class="nav-link">Pedidos</router-link>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled">Contacto</a>
            </li>
            </ul>
          </div>
        </nav>
        </div>
      
    </div>
  <router-view></router-view>
</template>

<script>
  export default {
    name: 'App',
    
  }
</script>


