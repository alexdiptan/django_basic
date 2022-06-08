$(document).ready(function(){
   // $('.basket_list input[type=number]').click(function(){
   //  $('.basket_list').click(function(){
    $('.basket_list').on('click', 'input[type=number]', function(){
       let pk = event.target.name;
       let quantity = event.target.value;
       $.ajax({
           url: '/basket/edit/' + pk + '/' + quantity + '/',
           succcess: function(data){
               // console.log(data);
               $('.basket_list').html(data.result)
           }
       });
   });
});