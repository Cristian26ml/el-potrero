// apps/core/static/core/js/main.js

document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('usuariosChart').getContext('2d');

    const roles = JSON.parse(document.getElementById('roles-data').textContent);
    const cantidades = JSON.parse(document.getElementById('cantidades-data').textContent);

    new Chart(ctx, {
        type: 'pie', // puedes cambiar a 'bar'
        data: {
            labels: roles,
            datasets: [{
                label: 'Usuarios por rol',
                data: cantidades,
                backgroundColor: [
                    '#FFD700', // dorado
                    '#000000', // negro
                    '#1E90FF', // azul
                    '#32CD32'  // verde
                ],
                borderColor: '#fff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                }
            }
        }
    });
});
