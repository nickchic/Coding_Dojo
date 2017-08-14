$(document).ready(function(){

    $('#click > button').click(function(){

        alert("You Clicked!");

    });

    $('#hide > button').click(function(){

        $('#hide > p').hide();

    });

    $('#show > p').hide();

    $('#show > button').click(function(){

        $('#show > p').show();

    });

    $('#toggle > button').click(function(){

        $('#toggle > p').toggle("slow");

    });

    $('#slide_down > p').hide();

    $('#slide_down > button').click(function(){

        $('#slide_down > p').slideDown();

    });

    $('#slide_up > button').click(function(){

        $('#slide_up > p').slideUp();

    });

    $('#slide_toggle > button').click(function(){

        $('#slide_toggle > p').slideToggle();

    });

    $('#fade_in > p').hide();

    $('#fade_in  > button').click(function(){

        $('#fade_in  > p').fadeIn();

    });

    $('#fade_out  > button').click(function(){

        $('#fade_out  > p').fadeOut();

    });

    $('#add_class  > button').click(function(){

        $('#add_class  > p').addClass("red_text");

    });

    $('#before  > button').click(function(){

        $('#before  > p').before("<p> Another paragraph </p>");

    });

    $('#after > button').click(function(){

        $('#after  > p').after("<p> the jQuery after method </p>");

    });

    $('#append > button').click(function(){

        $('#append  > p').append(", and ever");

    });

    $('#html > button').click(function(){

        $('#html  > p').after("<div></div>");
        $('#html  > div').html("<ul> <li>This</li> <li>is</li> <li>a</li> <li>list</li> </ul");

    });

    $('#attr > button').click(function(){

        $('#attr  > p').attr("id","blue");

    });

    $('#val > button').click(function(){

        alert("The value in the text box is..." + $('#val  > input').val());

    });

    $('#text > button').click(function(){

        $('#text  > p').text("..so is this one :(");

    });


    $('#data').data("toDisplay","sweet data bro");

    $('#data > button').click(function(){

        $('#data  > p').after("<h4></h4>");
        $('#data  > h4').text($('#data').data("toDisplay"));

    });

});
