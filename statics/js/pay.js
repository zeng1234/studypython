$(document).ready(function(){
    $("#submit").click(function(){
        var merchantId = $("#merchantId").val();
        var subject = $("#subject").val();
        var transAmt = $("#transAmt").val();
        var outOrderId = $("#outOrderId").val();
        var body = $("#body").val();
        var outAcctId = $("#outAcctId").val();
        var payMethod = $("#payMethod").val();
        var defaultBank = $("#defaultBank").val();
        var channel = $("#channel").val();
        var cardAttr = $("#cardAttr").val();
        var signType = $("#signType").val();
        var returnUrl = $("#returnUrl").val();
        var notifyUrl = $("#notifyUrl").val();
        var detailUrl = $("#detailUrl").val();
        var version = $("#version").val();
        var order={
            "merchantId":merchantId,
            "subject":subject,
            "transAmt":transAmt,
            "outOrderId":outOrderId,
            "body":body,
            "outAcctId":outAcctId,
            "payMethod":payMethod,
            "defaultBank":defaultBank,
            "channel" :channel,
            "cardAttr":cardAttr,
            "signType" :signType,
            "returnUrl":returnUrl,
            "notifyUrl":notifyUrl,
            "detailUrl":detailUrl,
            "version":version};
        $.ajax({
            type:"post",
            url:"/bankpay",
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