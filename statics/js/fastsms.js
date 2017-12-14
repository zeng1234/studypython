$(document).ready(function(){
    $("#submit").click(function(){
        var merchantId = $("#merchantId").val();
        var inputCharset = $("#inputCharset").val();
        var service = $("#service").val();
        var subject = $("#subject").val();
        var transAmt = $("#transAmt").val();
        var outOrderId = $("#outOrderId").val();
        var body = $("#body").val();
        var outAcctId = $("#outAcctId").val();
        var payMethod = $("#payMethod").val();
        var bankId = $("#bankId").val();
        var bankCardNo = $("#bankCardNo").val();
        var cardType = $("#cardType").val();
        var signType = $("#signType").val();
        var realName = $("#realName").val();
        var notifyUrl = $("#notifyUrl").val();
        var cardId = $("#cardId").val();
        var phoneNo = $("#phoneNo").val();

        var version = $("#version").val();
        var order={
            "merchantId":merchantId,
            "subject":subject,
            "transAmt":transAmt,
            "outOrderId":outOrderId,
            "body":body,
            "outAcctId":outAcctId,
            "payMethod":payMethod,
            "bankId":bankId,
            "inputCharset" :inputCharset,
            "cardType":cardType,
            "signType" :signType,
            "service":service,
            "notifyUrl":notifyUrl,
            "bankCardNo":bankCardNo,
            "realName":realName,
            "cardId":cardId,
            "phoneNo":phoneNo,

            "version":version};
        $.ajax({
            type:"post",
            url:"/fastsms",
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