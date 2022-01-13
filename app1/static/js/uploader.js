function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
$(document).on('click', '#savebtn', function (event) {

    event.preventDefault();
    console.log('clicked now ')
    // var output = '';
    const csrftoken = getCookie("csrftoken");
    
    
    



    var nm = $('#username').val();
    console.log($('#ajax_image').val())
    var fl = new FormData();
    // var fils = $('#ajax_image')[0].files[0];
    var fd = ('file', $('#ajax_image')[0].files[0].name);
    fl.append('file' , $('#ajax_image')[0].files[0] )
    // fl.append( 'input' , $('#username').val())
    console.log('file', $('#ajax_image')[0].files)
    // console.log(nm)
    // console.log(fl)
    console.log(fl)

    var my_data
    // console.log(nm)
    if (nm == '') {
        console.log('this is empty plz field ')
    }
    if (fd == '') {
        console.log('this file also not upload')
    }
    else{
        // console.log(my_data);
        var filed = { uname : nm ,  file: fl} 

        $.ajax({
            url: "save_data",
            method: "POST",
            headers: { "X-CSRFToken": csrftoken },
            data: filed,
            contentType : false,
            processData: false,
            success: function (data){
                console.log(data)
            }
            
        })
        
    }
})

// $(function() {
//     $('#ajax_image').submit(upload);
// });



// $.ajax({
//     url: "save_data",
//     method: "POST",
//     data: my_data,
//     success: function (data) {
//         console.log(data)
//         if (data.status == "save") {
//             console.log("data has been submit successfuly")
//             // var x = data.client_data
//             // for (i = 0; i < x.length; i++) {
//             //     console.log(i)
//             //     output +=
//             //         `<tr>
//             //         <td>${x[i].id}</td>
//             //         <td>${x[i].user_name}</td>
//             //         <td class="img_style"><img src="/media/${x[i].image}" alt=""></td>
//             //     </tr>`


//             // }
// //             // $('#tbody').html(output);
// //             // $('form')[0].reset();

//         // }
// //         // else {
// //         //     console.log("data has not submit check the code again")
// //         //     // console.log(data.client_data)


//         }

//     }
// })