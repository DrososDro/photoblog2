function showLoading(divId) {
  // Get the loading div by its ID
  var loadingDiv = document.getElementById(divId)

  // If the loading div exists, set its display property to "block"
  if (loadingDiv) {
    loadingDiv.style.display = 'block'
  }
}
