// function searchWord()
//   const res = await axios.get()

$('form').on("submit", async (e) => {
  e.preventDefault();
  const req = {
    params: {
      search_word: $('input').val()
    }
  }
  const res = await axios.post("/", req);
  updateCaption(res.data.result)
})

function updateCaption(str) {
  let $msg = $('<p>')
  let msg_text = str.split("-").join(" ")
  $msg.text(msg_text)

  $('.message').html($msg)
}