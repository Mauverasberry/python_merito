$(document).ready(function() {
    let url = 'http://127.0.0.1:5000';
    let gameId;

    $('#new-game').click(function() {
        $.post(url + '/game', function(data) {
            gameId = data.game_id;
            $('.cell').text('');
            updateGameStatus(gameId);
            $('#game-setup').hide();
            $('#game-container').show();
        });
    });

    $('#join-game').click(function() {
        gameId = $('#game-id-input').val();
        if (gameId) {
            updateGameStatus(gameId);
            $('#game-setup').hide();
            $('#game-container').show();
        } else {
            alert("Please enter a Game ID.");
        }
    });

    $('.cell').click(function() {
        const cellIndex = $(this).data('cell-index');
        makeMove(gameId, cellIndex);
    });

    function makeMove(gameId, cellIndex) {
        $.ajax({
            url: url + `/game/${gameId}/move`,
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ cellIndex }),
            success: function(response) {
                updateGameStatus(gameId);
            },
            error: function(response) {
                alert('Move could not be made. ' + response.responseText);
            }
        });
    }

    function updateGameStatus(gameId) {
        $.get(url + `/game/${gameId}`, function(data) {
            const moves = data.moves;
            $('.cell').text('');
            for (let i = 0; i < moves.length; i += 2) {
                const cellIndex = moves.charAt(i);
                const player = moves.charAt(i + 1);
                $(`.cell[data-cell-index=${cellIndex}]`).text(player);
            }
        });
    }

    setInterval(function() {
        if (gameId) {
            updateGameStatus(gameId);
        }
    }, 1000);
});
