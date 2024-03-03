var token = "";

var category_1_list = [];
var category_2_list = [];
var category_3_list = [];

var selectionCount = 0;

var result_list = [];

var option_1 = "";
var option_2 = "";
var option_3 = "";

var tile_text_1 = [];
var tile_text_2 = [];
var tile_text_3 = [];

var correct_answers = 0;

function changeTileColor(element) {

    if (element.getAttribute("class") == "white_box" && selectionCount == 0) {
        element.setAttribute("class", "green_box");
        tile_text_1 = [];
        tile_text_1 = element.querySelectorAll("p");
        option_1 = tile_text_1[0].innerText;
        selectionCount++;
    }

    else if (element.getAttribute("class") == "white_box" && selectionCount == 1) {
        element.setAttribute("class", "green_box");
        tile_text_2 = [];
        tile_text_2 = element.querySelectorAll("p");
        option_2 = tile_text_2[0].innerText;
        selectionCount++;
    }

    else if (element.getAttribute("class") == "white_box" && selectionCount == 2) {
        element.setAttribute("class", "green_box");
        tile_text_3 = [];
        tile_text_3 = element.querySelectorAll("p");
        option_3 = tile_text_3[0].innerText;
        selectionCount++;
    }

    else if (element.getAttribute("class") == "green_box" && selectionCount == 3) {
        element.setAttribute("class", "white_box");
        option_3 = "";
        selectionCount--;
    }

    else if (element.getAttribute("class") == "green_box" && selectionCount == 2) {
        element.setAttribute("class", "white_box");
        option_2 = "";
        selectionCount--;
    }

    else if (element.getAttribute("class") == "green_box" && selectionCount == 1) {
        element.setAttribute("class", "white_box");
        option_1 = "";
        selectionCount--;
    }

    if (selectionCount == 3) {
        result_list = [];
        result_list = [option_1, option_2, option_3];

        data = {
           'pk' : result_list,
           'c1' : category_1_list,
           'c2' : category_2_list,
           'c3' : category_3_list,
            "csrfmiddlewaretoken": token
        }

        $.post("check_results/", data, 
            function(response){
                if (response.status == 'Correct') {
                    for (var elem of document.querySelectorAll(".green_box")) {
                        elem.setAttribute("class", "gold_box");
                      }
                      correct_answers++;
                      document.getElementById("layout").setAttribute("class", "layout" + correct_answers.toString());
                      showAnswer(result_list, response.category);
                      selectionCount = 0;
                } else {
                    // Do something with errors
                }
        });
    }
} 

function showAnswer(results, correct_category) {
    if (correct_answers == 1) {
        var elem = document.getElementById("answer_box1")
        elem.setAttribute("class", "answer_box");
        elem.innerText = correct_category + "\n" + results[0] + ", " + results[1] + ", " + results[2];
    }
    else if (correct_answers == 2) {
        var elem = document.getElementById("answer_box2")
        elem.setAttribute("class", "answer_box");
        elem.innerText = correct_category + "\n" + results[0] + ", " + results[1] + ", " + results[2];
    }
    else if (correct_answers == 3) {
        var elem = document.getElementById("answer_box3")
        elem.setAttribute("class", "answer_box");
        elem.innerText = correct_category + "\n" + results[0] + ", " + results[1] + ", " + results[2];
    }
}