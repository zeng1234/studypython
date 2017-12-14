$(document).ready(function(){
    $("#submit").click(function(){
        var merchantId = $("#merchantId").val();
        var service = $("#sservice").val();
        var inputCharset = $("#inputCharset").val();
        var outOrderId = $("#outOrderId").val();

        var signType = $("#signType").val();
        var version = $("#version").val();
        var order={
            "merchantId":merchantId,
            "subject":service,
            "transAmt":inputCharset,
            "outOrderId":outOrderId,
            "signType" :signType,
            "version":version};
        $.ajax({
            type:"post",
            url:"/orderquery",
            data:order,
            cache:false,
            success:function(data){
                 $(document).html(data);
            },
            error:function(){
                alert("error!");
            },
        });
    });
});