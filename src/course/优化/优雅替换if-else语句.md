

[toc]



## 场景
日常开发，if-else语句写的不少吧？？当逻辑分支非常多的时候，if-else套了一层又一层，虽然业务功能倒是实现了，但是看起来是真的很不优雅，尤其是对于我这种有强迫症的程序"猿"，看到这么多if-else，脑袋瓜子就嗡嗡的，总想着解锁新姿势：干掉过多的if-else！！！本文将介绍三板斧手段：

优先判断条件，条件不满足的，逻辑及时中断返回；
融入策略模式；
策略模式+工厂+单例模式，锦上添花；
接下来先附上一段很久以前自己写的业务代码，核心逻辑就是在支付回调中根据用户购买的价格包赋予用户对应的权益(VIP视频会员天数+抽奖机会次数)。我的天，太多if-else了……(看不清楚可以点击图片放大)

![在这里插入图片描述](https://img-blog.csdnimg.cn/31d1f4d481774946b0e54794c4c92060.png)

### 1.优先判断条件，不满足及时中断

这点非常容易理解，就是说在业务逻辑里面，先把不符合条件的给先过滤掉，而不是层层嵌套if-else判断，结合代码图看一下：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/460f3f07058647299381d99df447c95b.png)

![](https://img-blog.csdnimg.cn/20200318225549224.png)

### 2.策略模式改造

先用策略模式替换掉文章开头讲到的，用户充值后根据价格包(付的多少钱)给用户增加VIP天数及抽检机会次数的逻辑，我这里就简化成"根据-价格包区分给用户增加不同的体育会员视频VIP天数"这个动作来讲解：

![](https://img-blog.csdnimg.cn/20200318230622524.png)
![](https://img-blog.csdnimg.cn/20200318230658743.png)
![](https://img-blog.csdnimg.cn/20200318230730792.png)

![](https://img-blog.csdnimg.cn/20200318230758682.png)

![](https://img-blog.csdnimg.cn/20200318230905627.png)


表面上看，代码稍微优雅了点，但是还是没和if-else彻底说拜拜，且recharge()充值方法可单独拎出来，只需要根据priceCode实例化不同的策略对象即可：

![](https://img-blog.csdnimg.cn/20200318231800248.png)

### 3.策略模式+工厂+单例模式，锦上添花

接下来使用"工厂类+单例"来给代码加点料:

![](https://img-blog.csdnimg.cn/20200319100452404.png)

![](https://img-blog.csdnimg.cn/20200319094242507.png)

![](https://img-blog.csdnimg.cn/2020031910035996.png)


![在这里插入图片描述](https://img-blog.csdnimg.cn/dfd2e6a3bf784207bcd1427c0fb78790.png)


blog.csdn.net/fanrenxiang/article/details/104955363

