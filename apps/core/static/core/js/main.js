// apps/core/static/core/js/main.js

document.addEventListener("DOMContentLoaded", function () {
    // --- Gráfico de roles ---
    const ctxRoles = document.getElementById('usuariosChart').getContext('2d');

    const roles = JSON.parse(document.getElementById('roles-data').textContent);
    const cantidades = JSON.parse(document.getElementById('cantidades-data').textContent);

    new Chart(ctxRoles, {
        type: 'pie',
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

    // --- Gráfico de inscripciones por mes ---
    const inscripcionesChartEl = document.getElementById('inscripcionesChart');
    if (inscripcionesChartEl) {
        const meses = JSON.parse(document.getElementById('meses-data').textContent);
        const totales = JSON.parse(document.getElementById('totales-data').textContent);

        new Chart(inscripcionesChartEl.getContext('2d'), {
            type: 'line',
            data: {
                labels: meses,
                datasets: [{
                    label: 'Inscripciones por mes',
                    data: totales,
                    borderColor: '#FFD700',
                    backgroundColor: 'rgba(255,215,0,0.2)',
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: '#FFD700' }
                    },
                    x: {
                        ticks: { color: '#FFD700' }
                    }
                }
            }
        });
    }
});
