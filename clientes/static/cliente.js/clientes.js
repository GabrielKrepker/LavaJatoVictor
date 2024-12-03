function add_carro() {
    const container = document.getElementById('form-carro');
    const html = `
        <div class="row">
            <div class="col-md">
                <input type="text" placeholder="Carro" class="form-control" name="carro">
            </div>
            <div class="col-md">
                <input type="text" placeholder="Placa" class="form-control" name="placa">
            </div>
            <div class="col-md">
                <input type="number" placeholder="Ano" class="form-control" name="ano">
            </div>
        </div>`;
    container.innerHTML += html;
}

let lastScrollTop = 0;
const footer = document.querySelector('.root-bar-bottom');

window.addEventListener('scroll', function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        footer.style.transform = 'translateY(100%)';
    } else {
        footer.style.transform = 'translateY(0)';
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});
