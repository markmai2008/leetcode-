LeetCode 解题记录
=================

| 编号 | 名称                       | 完成日期   | 简要题解                                               |  难度  |
| ---- | --------------------------| ---------- | ------------------------------------------------------| ------ |
| 0001 | 两数之和                   | 2020-07-12 | 暴力算法                                               |   ★  |
| 0002 | 两数相加                   | 2022-08-05 | 链表                                                  |  ★★  |
| 0003 | 无重复字符的最长子串        | 2022-10-16 | while循环                                             |  ★    |
| 0004 | 寻找两个正序数组的中位数    | 2022-10-23 | 分情况讨论                                             | ★★★ |
| 0005 | 最长回文子串               | 2022-10-23 | 经典算法                                               | ★★★ |
| 0006 | N 字形变换                 | 2022-10-23 | 分情况讨论                                             | ★★★ |
| 0007 | 整数反转                   | 2020-08-02 | 字符串，类型转换                                       |  ★    |
| 0008 | 字符串转换整数              | 2021-02-07 | 经典字符串转整数处理                                   | ★★   |
| 0009 | 回文数                     | 2020-08-02 | 字符串处理                                             | ★    |
| 0010 | 正则表达式匹配              | 2022-10-30 | 经典算法                                              | ★    |
| 0011 | 盛最多水的容器              | 2022-10-06 | while算法                                             | ★★    |
| 0012 | 整数转罗马数字              | 2022-10-06 | 分情况讨论                                             | ★    |
| 0013 | 罗马数字转整数              | 2022-06-12 | 经典算法                                              | ★    |
| 0014 | 最长公共前缀               | 2020-08-06 | 多层遍历                                               | ★    |
| 0015 | 三数之和                   | 2022-10-03 | 枚举算法                                               | ★★    |
| 0016 | 最接近的三数之和            | 2022-10-30 | for，while循环                                        | ★    |
| 0017 | 电话号码的字母组合          | 2022-12-18 | 多层遍历                                               | ★    |
| 0018 | 四数之和                   | 2022-12-18 | 超级多层遍历                                           | ★★    |
| 0019 | 删除链表的倒数第 N 个结点   | 2021-03-13 | 链表做题                                               | ★    |
| 0020 | 有效的括号                 | 2021-09-12 | for，if，elif循环                                      | ★    |
| 0021 | 合并两个有序链表            | 2021-04-03 | 总是比较两个链表头结点较小的那个放入新的链表              | ★    |
| 0026 | 删除排序数组中的重复项      | 2020-08-16 | 双指针                                                 | ★    |
| 0028 | 实现strStr（）             | 2021-02-08 | 二层循环，O((n-m)*n)                                   | ★    |
| 0036 | 有效的数独                 | 2020-12-20 | 枚举遍历，使用zip函数和集合判重                        | ★    |
| 0038 | 外观数列                   | 2021-02-28 | 单次循环，分段结算                                     | ★★   |
| 0048 | 旋转图像                    | 2021-01-03 | 二维数组，坐标转换，找规律，从一般到特殊，O(n*n)       | ★★   |
| 0053 | 最大子序和                  | 2020-08-08 | 分治法，原位算法，类似归并排序的思路，O(n*log(n))      | ★★   |
| 0066 | 加一                       | 2020-11-01 | 进制数的拆解与组装                                     | ★    |
| 0098 | 验证二叉搜索树              | 2021-04-18 | 中序遍历记住最后一个与当前遍历                          | ★   |
| 0101 | 对称二叉树                 | 2021-05-02 | 双节点递归，O(n)                                       | ★   |
| 0102 | 二叉树的层序遍历            | 2021-05-02 | 树的遍历，附加一个深度参数                             | ★★   |
| 0104 | 二叉树的最大深度            | 2021-04-18 | 二叉树遍历，后序遍历                                   | ★   |
| 0121 | 买卖股票的最佳时期 I        | 2020-09-26 | 贪心算法求最大值，遍历一次，O(n)                       | ★★   |
| 0122 | 买卖股票的最佳时期 II       | 2020-10-01 | 遍历一次，累加相邻增加值，O(n)                         | ★★   |
| 0125 | 验证回文串                 | 2021-02-07 | 经典算法                                               | ★    |
| 0136 | 只出现一次的数字            | 2020-10-18 | 异或运算                                               | ★    |
| 0141 | 环形链表                   | 2021-04-03 | 快慢指针                                              | ★★   |
| 0167 | 两数之和 II - 输入有序数组  | 2020-07-26 | 二分查找法，枚举一个，查找另一个，O(n*log(n))          | ★★   |
| 0189 | 旋转数组                   | 2020-10-01 | 循环k次，每次将最后一个弹出插入位置0                   | ★    |
| 0217 | 存在重复元素               | 2020-10-02 | 排序预处理，单词遍历判断相邻元素是否重复，O(n*log(n))  | ★    |
| 0234 | 回文链表                   | 2021-04-03 | 递归保存顺序内容和逆序内容                            | ★    |
| 0242 | 有效的字母异位词            | 2021-01-31 | 字母计数，O(n)                                         | ★    |
| 0283 | 移动零                     | 2020-12-20 | 双指针，O(n)                                           | ★    |
| 0350 | 两个数组的交集II            | 2020-10-25 | 排序后双指针，O(n*log(n)+m*log(m)+m+n),整体 O(mlog(m)) | ★    |
| 0387 | 字符串中的第一个唯一字符    | 2021-01-10 | 遍历一次记录字母出现的次数，再遍历一次输出结果，O(n)   | ★    |
| 1913 | 两个数对之间的最大乘积差    | 2023-07-13 | 遍历列表，将列表的最大值与第二大值之积减去列表的最小值与第二小值之积 | ★ |
