// apps/core/static/core/js/main.js

document.addEventListener("DOMContentLoaded", function () {
    const GOLD = '#DAA520';
    const GOLD_LIGHT = '#F6D365';
    const GOLD_PALE = '#FBF5B7';
    const GOLD_DARK = '#AA771C';
    const TEXT_MUTED = 'rgba(255,255,255,0.45)';
    const GRID_COLOR = 'rgba(218,165,32,0.08)';

    Chart.defaults.font.family = "Arial, sans-serif";
    Chart.defaults.color = TEXT_MUTED;

    const ctxRolesEl = document.getElementById('usuariosChart');
    if (ctxRolesEl) {
        const ctxRoles = ctxRolesEl.getContext('2d');
        const roles = JSON.parse(document.getElementById('roles-data').textContent);
        const cantidades = JSON.parse(document.getElementById('cantidades-data').textContent);

        new Chart(ctxRoles, {
            type: 'doughnut',
            data: {
                labels: roles,
                datasets: [{
                    label: 'Usuarios por rol',
                    data: cantidades,
                    backgroundColor: [GOLD_LIGHT, GOLD, GOLD_DARK, 'rgba(218,165,32,0.25)'],
                    borderColor: '#0d0d0d',
                    borderWidth: 3,
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: TEXT_MUTED,
                            font: { size: 11, family: "Arial" },
                            padding: 16,
                            usePointStyle: true,
                            pointStyle: 'circle'
                        }
                    },
                    tooltip: {
                        backgroundColor: '#0d0d0d',
                        borderColor: 'rgba(218,165,32,0.3)',
                        borderWidth: 1,
                        titleColor: GOLD_LIGHT,
                        bodyColor: '#fff',
                        padding: 12,
                        cornerRadius: 8
                    }
                }
            }
        });
    }

    const inscripcionesChartEl = document.getElementById('inscripcionesChart');
    if (inscripcionesChartEl) {
        const meses = JSON.parse(document.getElementById('meses-data').textContent);
        const totales = JSON.parse(document.getElementById('totales-data').textContent);

        const ctx = inscripcionesChartEl.getContext('2d');
        const gradient = ctx.createLinearGradient(0, 0, 0, 220);
        gradient.addColorStop(0, 'rgba(246,211,101,0.25)');
        gradient.addColorStop(1, 'rgba(246,211,101,0)');

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: meses,
                datasets: [{
                    label: 'Inscripciones',
                    data: totales,
                    borderColor: GOLD_LIGHT,
                    backgroundColor: gradient,
                    fill: true,
                    tension: 0.35,
                    pointBackgroundColor: '#0d0d0d',
                    pointBorderColor: GOLD_LIGHT,
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    pointHoverRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#0d0d0d',
                        borderColor: 'rgba(218,165,32,0.3)',
                        borderWidth: 1,
                        titleColor: GOLD_LIGHT,
                        bodyColor: '#fff',
                        padding: 12,
                        cornerRadius: 8,
                        displayColors: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: GRID_COLOR, drawBorder: false },
                        ticks: { color: TEXT_MUTED, font: { size: 11 } }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: TEXT_MUTED, font: { size: 11 } }
                    }
                }
            }
        });
    }
});