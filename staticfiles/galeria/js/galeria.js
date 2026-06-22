document.addEventListener('DOMContentLoaded', () => {
    const btns = document.querySelectorAll('.filtro-btn');
    const items = document.querySelectorAll('.galeria-item[data-tipo]');

    btns.forEach(btn => {
        btn.addEventListener('click', () => {
            btns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filtro = btn.dataset.filtro;
            items.forEach(item => {
                if (filtro === 'todo' || item.dataset.tipo === filtro) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });
});