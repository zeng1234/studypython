$(document).ready(function(){
    $("#submit").click(function(){
        var merchantId = $("#merchantId").val();
        var inputCharset = $("#inputCharset").val();
        var service = $("#service").val();
        var transAmt = $("#transAmt").val();
        var outOrderId = $("#outOrderId").val();
        var outAcctId = $("#outAcctId").val();
        var payMethod = $("#payMethod").val();
        var orderId = $("#orderId").val();
        var signType = $("#signType").val();
        var verifyCode = $("#verifyCode").val();
        var order={
            "merchantId":merchantId,
            "transAmt":transAmt,
            "outOrderId":outOrderId,
            "outAcctId":outAcctId,
            "payMethod":payMethod,
            "orderId":orderId,
            "inputCharset":inputCharset,
            "signType":signType,
            "service":service,
            "verifyCode":verifyCode
        };
        $.ajax({
            type:"post",
            url:"/fastpay",
            data:order,
            cache:false,
            success:function(data){
                 $(document.body).html(data);
            },
            error:function(){
                alert("error!");
            },
        });
    });
});