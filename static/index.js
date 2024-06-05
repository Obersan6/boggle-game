
let score = 0;
let timeLeft = 60;
let timer = setInterval(handleTime, 1000);

// Handle form submission event
function handleTime() {
    if (timeLeft <= 0) {
        clearInterval(timer);
        endGame();
    } else {
        $('#timer').text(`Time left: ${timeLeft} seconds.`);
        timeLeft--;
    }
}

$('#guess-form').on('submit', getGuessWord);

// Get the guess word from the form (from the user submission), check if it matches & update the UI accordingly
async function getGuessWord(evt) {
    evt.preventDefault();
    const word = $('#word').val();
    
    try {
        const response = await axios.post('/check-word', { word: word });
        const result = response.data.result;
        
        if (result === "ok") {
            $('ul').append(`<li>The word "${word}" is correct!</li>`);
            score += word.length;
            $('h4').text(`SCORE: ${score}`);
        } else if (result === "not-on-board") {
            $('ul').append(`<li>"${word}" is not on the board!</li>`);
        } else if (result === "not-a-word") {
            $('ul').append(`<li>"${word}" is not a word!</li>`);
        } else if (result === "already-submitted") {
            $('ul').append(`<li>"${word}" has already been submitted!</li>`);
        } else {
            console.error('Unexpected result:', result);
        }
    } catch (error) {
        console.error('There was an error checking the word:', error);
    }
}

// End the game and send it to the server
async function endGame() {
    $('#timer').text('Time is up, the game is over!');
    $('#guess-form :input').prop('disabled', true);

    try {
        console.log(`Final score being sent: ${score}`);
        const response = await axios.post('/update-stats', new URLSearchParams({ score: score }));
        const data = response.data;

        $('#times-played').text(`Times played: ${data.numb_plays}`);
        $('#highest-score').text(`Highest score: ${data.highest_score}`);
        console.log(`Highest score received: ${data.highest_score}`);
    } catch (error) {
        console.error('Error updating stats: ', error);
    }
}


