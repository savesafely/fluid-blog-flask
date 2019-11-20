
$(window).scroll(function () {
    //下面这句主要是获取网页的总高度，主要是考虑兼容性所以把Ie支持的documentElement也写了，这个方法至少支持IE8
    var htmlHeight = $(document.body).height();
    console.log("网页总高度" + htmlHeight);

    //clientHeight是网页在浏览器中的可视高度，
    var clientHeight = $(window).height();
    console.log("可视高度：" + clientHeight);

    //scrollTop滚动条到顶部的垂直高度
    var scrollTop = $(document).scrollTop();
    console.log("滚动条位置：" + scrollTop);

    var pk = 1;


    //通过判断滚动条的top位置与可视网页之和与整个网页的高度是否相等来决定是否加载内容；

    if (Math.ceil(scrollTop+clientHeight)>=htmlHeight){
        alert("我已经到底部啦");
        pk = pk +1; //每次和后端交互，page+1。
        addListMore(pk);
    }
    if (scrollTop <=0){
        refresh();
    }

});



function addListMore(pk) {
    console.log("加载更多");
    $.ajax({
        type:"GET",
        url:"/ajax",
        data:{
        page:pk
        },

        dataType:"html",
        success:function (data) {

            console.log(data);

            var div = document.createElement("div");
            document.body.appendChild(div);
            div.innerHTML = data;

        }

    })
}

function refresh() {
    $.ajax({
        type:"GET",
        url:"/",
        dataType:"html",
        success:function () {
            window.location.reload();
            //location.href = url + "/teacherList";


        }
    })

}


//$(function () {
//    $("#submit").click(function (event) {
//        event.preventDefault();
//        var userInput = $('input[name="user"]');
//        var user = userInput.val();
//        var pwdInput = $("input[name='pwd']");
//        var pwd = pwdInput.val();
//        $.post({
//            'url': '/login',
//            'data': {
//                'user': user,
//                'pwd': pwd
//            },
//            "success": function (data) {
//                if (data['code'] == 200) {
//                    window.location = '/home'
//                } else {
//                    var error = data['error'];
//                    $("#error").html(error);
//                    $("#error").show();
//                }
//            },
//            'fail': function (error) {
//                consle.log(error)
//            }
//        });
//    });
//});
