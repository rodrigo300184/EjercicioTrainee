const btndelete = document.querySelectorAll('.btn-delete')

if (btndelete) {

    const btnArray = Array.from(btndelete);
    btnArray.forEach((btn) => {

        btn.addEventListener('click', (e) => {
            if (!confirm('¿Está seguro que desea eliminar el registro?')) {
                e.preventDefault();
            }
        });
    });

}