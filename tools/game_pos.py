class CommonPos():
    second_position = (1000, 100), (1111, 452)  # The second settlement point

    @staticmethod
    def InitPosWithClient__():
        for item in vars(CommonPos).items():
            if not '__' in item[0]:
                setattr(CommonPos, item[0], ((
                    item[1][0][0], item[1][0][1] + 35), (item[1][1][0], item[1][1][1] + 35)))


class TansuoPos():
    last_chapter = (934, 493), (1108, 572)  # List of the last chapter
    quit_last_chapter = (913, 114), (948, 148)  # Exit the last chapter
    tansuo_btn = (787, 458), (890, 500)  # Exploration button
    tansuo_denglong = (424, 118), (462, 158)  # Exploration lantern
    ready_btn = (1000, 460), (1069, 513)  # Preparation button
    quit_btn = (32, 45), (58, 64)  # Exit copy
    confirm_btn = (636, 350), (739, 370)  # Exit confirmation button
    change_monster = (427, 419), (457, 452)  # Switch dog food click area
    quanbu_btn = (37, 574), (80, 604)  # "All" button
    n_tab_btn = (142, 288), (164, 312)  # N card tag
    s_tab_btn = (33, 264), (82, 307)  # Material label
    r_tab_btn = (216, 322), (259, 366)  # R card label
    n_slide = (168, 615), (784, 615)  # N card progress bar, from beginning to end
    gouliang_left = (161, 174), (322, 288)  # Left dog food location
    gouliang_middle = (397, 218), (500, 349)  # Intermediate dog grain position
    gouliang_right = (628, 293), (730, 430)  # Right dog position
    gouliang_leftback = (0, 273), (150, 393)  # Left rear dog grain position
    gouliang_rightback = (433, 462), (567, 569)  # Right behind dog food position
    yaoqing_comfirm = (601, 361), (746, 406)  # Continue invitation button

    @staticmethod
    def InitPosWithClient__():
        for item in vars(TansuoPos).items():
            if not '__' in item[0]:
                setattr(TansuoPos, item[0], ((
                    item[1][0][0], item[1][0][1] + 35), (item[1][1][0], item[1][1][1] + 35)))


class YuhunPos():
    tiaozhan_btn = (995, 533), (1055, 595)    # Royal Soul Challenge Button
    kaishizhandou_btn = (1048, 535), (1113, 604)   # Royal soul begins fight button
    yuhun_menu = (148, 568), (206, 620)    # Royal soul menu
    yuhun_btn = (147, 152), (327, 408)    # 魂 选
    yeyuanhuo_btn = (476, 125), (708, 427)    # Industry original fire option
    beimihu_btn = (838, 141), (1048, 407)    # Himself

    @staticmethod
    def InitPosWithClient__():
        for item in vars(YuhunPos).items():
            if not '__' in item[0]:
                setattr(YuhunPos, item[0], ((
                    item[1][0][0], item[1][0][1] + 35), (item[1][1][0], item[1][1][1] + 35)))
