class Alert {
  #ALERT_DURATION = 3000

  constructor(category, message) {
    this.category = category
    this.message = message
  }

  #createAlertElement() {
    const alert = document.createElement('div')
    alert.className = `alert is-${this.category}`
    alert.textContent = this.message

    return alert
  }

  show(queryContainer = '#alerts') {
    const alertsContainer = document.querySelector(queryContainer)
    if (!alertsContainer) {
      console.error('Não encontrou o container de alerts!')
      return
    }

    const alert = this.#createAlertElement()
    alertsContainer.appendChild(alert)

    setTimeout(() => alert.remove(), this.#ALERT_DURATION)
  }
}

document.body.addEventListener('alerts', (event) => {
  const alerts = event.detail.value
  alerts.forEach(([category, message]) => {
    const alert = new Alert(category, message)
    alert.show()
  })
})
