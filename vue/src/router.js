import { createRouter, createWebHistory } from "vue-router";

import PrograMadores from './pages/PrograMadores';
import LengProg from './pages/LengProg';
import Pedido from './pages/NuevoPedido';

const routes = [
    {
        name: 'programadores',
        path: '/',
        component: PrograMadores,
    },
    {
        name: 'lenguajes',
        path: '/lenguajes',
        component: LengProg,
    },
    {
        name: 'pedido',
        path: '/pedido',
        component: Pedido,
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes:routes
})

export default router