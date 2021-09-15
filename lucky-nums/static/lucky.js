const BASE_URL = "http://localhost:5000/api/get-lucky-num";

/** processForm: get data from form and make AJAX call to our API. */

function processForm(evt) {
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    return `
    <div>
    Your lucky number is ${resp.num.num} (${resp.num.fact})
    </div>
    <div>
    Your birth year (${resp.year.year}) fact is ${resp.year.fact}
    </div>
    ;`

}


// $("#lucky-form").on("submit", processForm);


$("#lucky-form").on("submit", async function (evt) {
    evt.preventDefault();
  
    let name = $("#name").val();
    let year = $("#year").val();
    let email = $("#email").val();
    let color = $("#color").val();

    const luckyNumResponse = await axios.post(`${BASE_URL}`, {
        name,
        year,
        email,
        color
    })
    console.log(luckyNumResponse);

    if ("errors" in luckyNumResponse.data){
        $("#name-err").append(luckyNumResponse.data.errors.name)
        $("#year-err").append(luckyNumResponse.data.errors.year.join('; '))
        $("#email-err").append(luckyNumResponse.data.errors.email)
        $("#color-err").append(luckyNumResponse.data.errors.color.join('; '))
    }
    else{
        let luckyNum = $(handleResponse(luckyNumResponse.data));
        $("#lucky-results").append(luckyNum);
        $("#lucky-form").trigger("reset");
    }
})

