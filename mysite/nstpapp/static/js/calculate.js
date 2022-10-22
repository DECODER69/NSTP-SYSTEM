const calculate = () => {


    // let td_count = document.querySelector("#count").innerHTML;
    // console.log(td_count)

    // let td1 = document.querySelector('.td1').value;
    // let td2 = document.querySelector('.td2').value;
    // let td3 = document.querySelector('.td3').value;



    // console.log(td1, td2)
    // sum = parseFloat(td1) + parseFloat(td2) + parseFloat(td3);

    // final = (sum / td_count * 100 * 0.3);
    // console.log("final to  " + final)
    // console.log(sum)

    // if (final != '') {
    //     document.querySelector("#result").innerHTML = final;
    // } else {
    //     document.querySelector("#showdata").innerHTML = "0";
    // }
    var td_count = $("#count").text();
    // alert(td_count)
    $(document).ready(function() {

        $('tr').each(function() {
            var results = 0;


            $(this).find('.tds').each(function() {
                var marks = $(this).text();


                if (marks.length !== 0) {
                    results += parseFloat((marks / td_count * 100 * 0.3).toFixed(2));
                    // alert(sums)
                    console.log(results.toFixed(2));




                }
            });
            $(this).find('.result').html(results);
            $(this).find('#input').val(results);

        })


    });


};