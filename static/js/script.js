document.querySelectorAll(".device").forEach(btn => {
    console.log(btn)
    btn.addEventListener("click", (e) => {
      const id = btn.getAttribute("data-id")
      console.log(id)
    })
})

function control(id) {
    const requestConfig = {method: "POST", headers: new Headers()}
    fetch(`/control/{$id}`, requestConfig)
    .then(response => response.json())
    .then(response => {
        if(response.success === 'ok') {
            console.log('ok')
        }
      }).catch(error => {
        console.log({html: 'Erro ao deletar filme'})
      })
}