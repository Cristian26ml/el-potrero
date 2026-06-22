document.addEventListener('DOMContentLoaded', () => {
    const filtros = document.querySelectorAll('.cal-filtro');
    const eventos = document.querySelectorAll('.evento[data-tipo]');

    filtros.forEach(btn => {
        btn.addEventListener('click', () => {
            filtros.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filtro = btn.dataset.filtro;
            eventos.forEach(ev => {
                if (filtro === 'todo' || ev.dataset.tipo === filtro) {
                    ev.classList.remove('hidden');
                } else {
                    ev.classList.add('hidden');
                }
            });
        });
    });
});