
var myWordList;	
console.log("flt");

var xhr = new XMLHttpRequest();
//xhr.onreadystatechange = handleStateChange; // Implemented elsewhere.
xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
        myWordList = JSON.parse(xhr.responseText);
        whole_text = document.body.innerHTML;

        console.log(myWordList);
        json_words = myWordList.all_words;
        console.log(json_words[0]);
        for(var x=0;x<json_words.length;x++)
        {
        	//console.log(json_words[x])
        //	word= JSON.parse(json_words[x]);
        	current_word=json_words[x].word;

        	whole_text.highlight(current_word);
        }


        //myFunction(myArr);
    }
};

xhr.open("GET", chrome.extension.getURL('/words.json'), true);
xhr.send();

//words_list = myWordList
//cosole.log(words_list)