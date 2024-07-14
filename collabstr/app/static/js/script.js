// script.js

$(document).ready(function() {

    $('.tab-link').on('click', function(event) {
        event.preventDefault();  // Prevent the default link behavior

        $('.tab-link').removeClass('active');
        $(this).addClass('active');

        const platform = $(this).data('platform');
        const url = `${window.location.origin}/collabs/app/${platform}/`;

        window.location.href = url;

    });
    
    $(document).ready(function() {
        $('#content-list').on('click', '.download-btn', function() {
            const url = $(this).data('url');
            console.log('La URL es:', url);
            
            const downloadLink = document.createElement('a');
            downloadLink.href = url;
            downloadLink.setAttribute('download', ''); 
            downloadLink.style.display = 'none';
            
            document.body.appendChild(downloadLink);
            downloadLink.click();

            document.body.removeChild(downloadLink);
        });
    });
    
    
    $('#content-list').on('click', '.play-btn', function() {
        const videoId = $(this).data('video-id');
        const videoElement = document.getElementById('video-player-' + videoId);
        
        if (videoElement) {
            if (videoElement.paused) {            
                $(this).html('<i class="fas fa-pause"></i>');
                videoElement.play();
            } else {
                videoElement.pause();
                $(this).html('<i class="fas fa-play"></i>');
            }
        }
    });

    var $backToTopBtn = $('#scrollToTopBtn');
    
    if ($(document).scrollTop() > 100) {
        $backToTopBtn.fadeIn();
    } else {
        $backToTopBtn.fadeOut();
    }
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $backToTopBtn.fadeIn();
        } else {
            $backToTopBtn.fadeOut();
        }
    });
    $backToTopBtn.click(function() {
        $('html, body').animate({ scrollTop: 0 }, 'slow');
    });


});
