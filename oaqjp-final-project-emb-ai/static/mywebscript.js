let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let res = JSON.parse(xhttp.responseText);
            let responseText = 'For the given statement, the system response is ';
            for (let i = 0; i < Object.keys(res).length; i++) {
                if (Object.keys(res)[i] !== 'dominant_emotion') {
                    if (i == Object.keys(res).length-2) {
                        responseText += `'${Object.keys(res)[i]}': ${res[Object.keys(res)[i]]} and `;
                    } else if (i == Object.keys(res).length-1) {
                        responseText += `'${Object.keys(res)[i]}': ${res[Object.keys(res)[i]]}. `;
                    } else {
                        responseText += `'${Object.keys(res)[i]}': ${res[Object.keys(res)[i]]}, `;
                    }
                }
            }
            responseText += `The dominant emotion is  <strong>${res['dominant_emotion']}</strong>.`
            document.getElementById("system_response").innerHTML = responseText;
        } else {
            document.getElementById("system_response").innerHTML = JSON.parse(xhttp.responseText)['message'];
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
