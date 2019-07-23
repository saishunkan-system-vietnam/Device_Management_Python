// function conn() {
//     var socket = new WebSocket('ws://127.0.0.1:8000/ws_brand/')
//     console.log(socket)
//     socket.onopen
//     socket.onmessage = function (e) {
//         var data = JSON.parse(e.data);
//         var html = '';
//         for (var i = 0; i < data.length; i++) {
//             var url = "{% url 'brand:edit' 999999 %}".replace(/999999/, data[i].pk.toString());
//             html += `<tr>
//                     <td>${data[i].pk}</td>
//                     <td class="center">${data[i].fields.brand_name}</td>
//                     <td class="center">${data[i].fields.created_user}</td>
//                     <td class="center">${data[i].fields.update_user}</td>
//                     <td class="center">${data[i].fields.created_time}</td>
//                     <td class="center">${data[i].fields.update_time}</td>
//                     <td class="center">                                
//                         <a class="btn btn-info" href="${url}">
//                             <i class="glyphicon glyphicon-edit icon-white"></i>
//                             Edit
//                         </a>
//                         <button class="btn btn-delete btn-danger" id="${data[i].pk}">
//                             <i class="glyphicon glyphicon-trash icon-white"></i>
//                             Delete
//                         </button>
//                     </td>
//                 </tr>`;
//         }

//         document.getElementById("list-brand").innerHTML = html;
//     }    
// }
// conn();



////////////////////

document.addEventListener('DOMContentLoaded', function () {
    const webSocketBridge = new channels.WebSocketBridge();
    webSocketBridge.connect('/ws_brand/');
    webSocketBridge.listen(function (action, stream) {
        if (action.event == "Change brand") {
            // console.log('a')
            // var data = JSON.parse(action.brand);
            // var html = '';
            // for (var i = 0; i < data.length; i++) {
            //     var url = "{% url 'brand:edit' 999999 %}".replace(/999999/, data[i].pk.toString());
            //     html += `<tr>
            //             <td>${data[i].pk}</td>
            //             <td class="center">${data[i].fields.brand_name}</td>
            //             <td class="center">${data[i].fields.created_user}</td>
            //             <td class="center">${data[i].fields.update_user}</td>
            //             <td class="center">${data[i].fields.created_time}</td>
            //             <td class="center">${data[i].fields.update_time}</td>
            //             <td class="center">                                
            //                 <a class="btn btn-info" href="${url}">
            //                     <i class="glyphicon glyphicon-edit icon-white"></i>
            //                     Edit
            //                 </a>
            //                 <button class="btn btn-delete btn-danger" id="${data[i].pk}">
            //                     <i class="glyphicon glyphicon-trash icon-white"></i>
            //                     Delete
            //                 </button>
            //             </td>
            //         </tr>`;
            // }
            html=action.brand
            document.getElementById("list-brand").innerHTML = html;
        }
    })
    document.ws = webSocketBridge; /* for debugging */     
   
})