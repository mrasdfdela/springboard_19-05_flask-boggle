// sends word request to server and updates score/caption from response
$('form').on("submit", async (e) => {
  e.preventDefault();
  if ( parseInt($('.timer').text()) > 0 ) {
    const req = {
      params: {
        search_word: $('input').val()
      }
    }
    const res = await axios.post("/", req);
  
    updateScore(res.data.result);
    updateCaption(res.data.result);
    $('input').val('')
  }
})

function updateCaption(str) {
  let msg_text = str.split("-").join(" ");
  $('.message').text(msg_text);
}

function updateScore(str){
  let score = parseInt($('.score').text());
  if (str === 'ok') {
    let word_score = $('input').val().length;
    score += word_score;
  }
  
  $('.score').text(score);
  $('.scoreBoard').show();
}

// sets countdown timer for boggle game
window.setInterval(()=>{
  let time = parseInt($('.timer').text());
  if (time > 0) {
    time -= 1
    $('.timer').text(time);
  } else {
    $('.timer').toggleClass("time_expired")
  }
},1000)

// sends high score at end of game
window.setTimeout(async () => {
  current_score = parseInt($('.score').text());
  const req = {
    params: {
      new_score: current_score
    }
  }
  const res = await axios.post("/score_board", req);
  console.log(res.data);
},parseInt($('.timer').text())*1000);