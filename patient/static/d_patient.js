
const progress = document.querySelectorAll('.health-condition .cards .card .progress')
progress.forEach(item => {
    item.style.setProperty('--value', item.dataset.value)
})

const sidebar = document.querySelector('.wrapper #sidebar')
const navToggler = document.querySelector('#navbar .sidebar-toggler .fa-solid')
const main = document.querySelector('.main-content')

navToggler.addEventListener('click', () => {
    sidebar.classList.toggle('hide')
    main.classList.toggle('fullWidth')
})
