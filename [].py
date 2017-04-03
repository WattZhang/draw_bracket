#!/usr/bin/env python
# coding=utf-8


# 括号绘制函数，num_draw控制绘制长度，drawflag控制绘制类型
def draw_bracket(num_draw, drawflag=1):
    # 初始化输出字符串
    draw_str = ''
    draw_width = (max_level - num_draw) * 2
    # 绘制对齐用的空格
    draw_str += ' ' * (num_draw - 1)
    # 绘制主体
    draw_str += '|'
    # 模式1在内部绘制line
    if drawflag == 1:
        draw_str += '+'
        draw_str += '-' * (draw_width - 1)
        draw_str += '+'
    # 模式2在内部绘制空格
    else:
        draw_str += ' ' * (draw_width + 1)
    draw_str += '|'
    return draw_str


# 边缘线绘制函数，num_draw控制绘制长度
def draw_line(num_draw_line):
    # 初始化输出字符串
    draw_line_str = ''
    # 绘制对齐用的空格
    draw_line_str += ' ' * num_draw_line
    draw_width = (max_level - num_draw_line) * 2
    # 绘制直线主体
    draw_line_str += '+'
    draw_line_str += '-' * (draw_width - 1)
    draw_line_str += '+'
    # 并不直接打印 返回字符串
    return draw_line_str


# 读入原始数据
str_in = raw_input().strip()

# 数据预处理
str_left = '['
str_right = ']'
max_level = 0  # 最大层数
temp_level = 0  # 嵌套层数暂存
level_list = [0]  # 嵌套层数列表
for str_i in str_in:
    if temp_level > max_level:
        max_level = temp_level
    if str_i == str_left:
        temp_level += 1
    if str_i == str_right:
        temp_level -= 1
    level_list.append(temp_level)
# 循环结束后生成了 level_list 代替str_in参加逻辑运算


for step_i in xrange(0, len(level_list)):
    # 括号边缘判断，外边绘制一次，内部边缘绘制两次
    if level_list[step_i] == 0:
        if step_i == 0 or step_i == len(level_list) - 1:
            print draw_line(0)
        else:
            print draw_line(0)
            print draw_line(0)
    # 非边缘时的逻辑
    else:
        # 判断是否为最小括号组，是的话，绘制括号组，不是则绘制边缘，传递drawflag=2时绘制空括号
        if str_in[step_i - 1] == str_left and str_in[step_i] == str_right:
            print draw_bracket(level_list[step_i], drawflag=2)
            print ''
            print draw_bracket(level_list[step_i], drawflag=2)
        else:
            if str_in[step_i - 1] == str_right and str_in[step_i] == str_left:
                print draw_line(level_list[step_i])
                print draw_line(level_list[step_i])
            else:
                print draw_bracket(level_list[step_i])
