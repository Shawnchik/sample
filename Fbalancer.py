###########################
# running log
###########################

# 5
#9.375 12.353515625 5.594199523329735 0.0874093675520271 0.04233891240801313 6.759316101670265 3.2740437367465347 1.8928065353065904
#242.8254275327832 -109.79538136063972 -109.79807023589557 -75.35934562683106 -91.43838921202487 -96.81246408217388
#6 6 6 6 6 6 6
#2.527639150619507

#10
#5.95703125 9.273195266723633 4.145176015299512 0.002024011726220465 0.0010120058631102324 5.128019251424121 2.406262939755166 1.404045025882531
#270.251430205578 -15.740726394142797 -15.740727930376597 3.1600123683881804 -5.52513963447058 -8.482153286528796
#11 11 7 11 1 11 11
#61.104543924331665

# 15
#6.2042236328125 9.300295682623982 4.158425359923257 6.345253539921962e-05 3.172626769960981e-05 5.141870322700726 2.413782355924802 1.408027430490864
#269.77945931152345 -16.71604047875013 -16.716040480259966 2.3057111487473634 -6.4338067439134665 -9.407618611435524
#16 16 6 16 1 16 16
#753.2379608154297

# 20
# 6.221485137939453 9.302404890559046 4.159368446472957 1.9833414299359117e-06 9.916707149679558e-07 5.143036444086089 2.414329776036202 1.4083594197685008
# 269.7454581321838 -16.789278615718953 -16.789278615720427 2.2411018451532954 -6.50238055602923 -9.477594938905233
# 21 21 6 21 1 16 21
# 735.1795928478241

# 25
# 6.221294403076172 9.302378889776719 4.159356820787464 6.197924644928371e-08 3.0989623224641857e-08 5.143022068989255 2.414323027838966 1.4083550875806579
# 269.74585021523467 -16.788402793728924 -16.788402793728924 2.241871285165402 -6.5015622389648655 -9.47675831803635
# 21 23 6 26 1 16 26

# 30
# 6.221294403076172 9.302378889776719 4.159356820787464 1.936851451540116e-09 9.68425725770058e-10 5.143022068989255 2.414323027838966 1.4083550999474823
# 269.74585021523467 -16.788402793728917 -16.788402793728917 2.241871285165402 -6.5015622389648655 -9.47675837028699
# 21 23 6 31 1 16 31
# 1418.7537770271301

#40
#6.221294403076172 9.302378889776719 4.159356820787464 1.8914564956446446e-12 9.457282478223223e-13 5.143022068989255 2.414323027838966 1.408355099573096
#269.74585021523467 -16.788402793728917 -16.788402793728917 2.241871285165402 -6.5015622389648655 -9.476758368705184
#21 23 6 41 1 16 41
#2321.424807548523


# 精度を0.01に
# 6.22100830078125 9.30239763983991 4.159507147794628 1.847192242629804e-15 9.23596121314902e-16 5.142890492045282 2.4144966836433297 1.4084563987919423
# 269.7447957033811 -16.78980614631803 -16.78980614631803 2.2418435374920307 -6.502847815494926 -9.478471956441876
# 17 19 5 51 1 12 81
# 2421.1230454444885

# 0.1 100 収束できない

# 0.1 100
#6.219482421875 9.302004845812917 4.160467011115543 1.6410148862653823e-30 8.205074431326911e-31 5.141537834697374 2.410095860014394 1.4058892516750632
#269.7386400996073 -16.78865405191968 -16.78865405191968 2.251780273719092 -6.461062807968691 -9.425849689931894
#15 17 5 101 1 5 101
#3383.8987185955048

# 30 30 30 20 20 20 20


import time
p0 = 101.3
s = time.time()

def two_room(g_2, dp_loss_oc):
    global p0
    # g_2 = g_bc
    # dp_loss_oc = dp_loss_ab + dp_fan1 + dp_loss_bc
    g_ce = 0
    g_jl = 0
    p1 = 0
    p2 = 0
    p3 = 0
    g_ce_max = g_2
    g_ce_min = 0
    dp_loss_ce = 10
    dp_loss_eg = 0
    dp_loss_hj = 0
    dp_loss_jl = 0
    dp_loss_kl = 0
    dp_loss_cd = 0
    c1 = 0
    while abs(dp_loss_ce + dp_loss_eg + dp_loss_hj + dp_loss_jl - dp_loss_kl - dp_loss_cd) > 0.001:
        g_ce = (g_ce_max + g_ce_min) / 2
        dp_loss_ce = -1.5 * g_ce ** 2

        g_eg_min = 0
        g_eg_max = g_ce
        dp_loss_eg = 10
        dp_loss_hj = 0
        dp_loss_ij = 0
        dp_loss_ef = 0
        c2 = 0
        while abs(dp_loss_eg + dp_loss_hj - dp_loss_ij - dp_loss_ef) > 0.001:
            g_eg = (g_eg_max + g_eg_min) / 2
            dp_loss_eg = -1.5 * g_eg ** 2
            p3 = p0 + dp_loss_oc + dp_loss_ce + dp_loss_eg
            g_draft3 = (abs(p3 - p0) / 100) ** 0.5 * (p3 - p0) / abs(p3 - p0)  # すき間風が部屋から出ていく方を流量正とする
            g_hj = g_eg - g_draft3

            if g_hj < 0:  # g_hiは逆流しないこととする。
                g_hj = 0
            dp_loss_hj = -1.5 * g_hj ** 2
            g_ef = g_ce - g_eg
            dp_loss_ef = -1.5 * g_ef ** 2
            p2 = p0 + dp_loss_oc + dp_loss_ce + dp_loss_ef
            g_draft2 = (abs(p2 - p0) / 100) ** 0.5 * (p2 - p0) / abs(p2 - p0)  # すき間風が部屋から出ていく方を流量正とする
            g_ij = g_ef - g_draft2
            if g_ij < 0:  # g_hiは逆流しないこととする。
                g_ij = 0
            dp_loss_ij = -1.5 * g_ij ** 2

            if dp_loss_eg + dp_loss_hj - dp_loss_ij - dp_loss_ef > 0:
                g_eg_min = g_eg
            else:
                g_eg_max = g_eg

            c2 += 1
            if c2 > 25:
                break

        g_cd = g_2 - g_ce
        dp_loss_cd = -1.5 * g_cd ** 2
        p1 = p0 + dp_loss_oc + dp_loss_cd
        g_draft1 = (abs(p1 - p0) / 100) ** 0.5 * (p1 - p0) / abs(p1 - p0)  # すき間風が部屋から出ていく方を流量正とする
        g_kl = g_cd - g_draft1
        if g_kl < 0:  # g_hiは逆流しないこととする。
            g_kl = 0
        dp_loss_kl = -1.5 * g_kl ** 2
        g_jl = g_hj + g_ij
        dp_loss_jl = -1.5 * g_jl ** 2
        if dp_loss_ce + dp_loss_eg + dp_loss_hj + dp_loss_jl - dp_loss_kl - dp_loss_cd > 0:
            g_ce_min = g_ce
        else:
            g_ce_max = g_ce

        c1 += 1
        if c1 > 25:
            break
    g_lm = g_jl + g_kl
    dp_c = dp_loss_ce + dp_loss_eg + dp_loss_hj + dp_loss_jl
    return (g_ce, g_lm, p1, p2, p3, c1, c2, dp_c)


dp_fan1 = 10
dp_fan2 = 0
dp_loss_0a0b = 0
dp_loss_0b0c = 0
dp_loss_0c1a = 0
dp_loss_1a2a = 0
dp_loss_2a3b = 0
dp_loss_3c2d = 0
dp_loss_2d1d = 0
dp_loss_1d0d = 0
dp_loss_0d0e = 0
dp_loss_0e0f = 0
g_0a0b_max = 200
g_0a0b_min = 0
cnt0 = 0

while abs(dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d +
          dp_loss_2d1d + dp_loss_1d0d + dp_fan2 + dp_loss_0d0e + dp_loss_0e0f) > 0.1:
    g_0a0b = (g_0a0b_max + g_0a0b_min) / 2
    dp_loss_0a0b = - 0.1 * g_0a0b ** 2

    g_0b0c_max = 200
    g_0b0c_min = g_0a0b
    dp_fan1 = 0
    dp_fan2 = 0
    dp_loss_0b0c = 10
    dp_loss_0c1a = 0
    dp_loss_1a2a = 0
    dp_loss_2a3b = 0
    dp_loss_3c2d = 0
    dp_loss_2d1d = 0
    dp_loss_1d0d = 0
    dp_loss_0d0e = 0
    dp_loss_0e0b = 0
    cnt1 = 0

    g_0e0b = 0
    g_0d0e = 0

    while abs(dp_fan1 + dp_loss_0b0c + dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d +
              dp_loss_1d0d + dp_fan2 + dp_loss_0d0e + dp_loss_0e0b) > 0.1:
        g_0b0c = (g_0b0c_max + g_0b0c_min) / 2
        dp_loss_0b0c = - 1.1 * g_0b0c ** 2
        dp_fan1 = 200 - 0.1 * g_0b0c ** 2

        g_0c1a_max = g_0b0c
        g_0c1a_min = 0

        cnt2 = 0

        dp_loss_0c1a = 10
        dp_loss_1a2a = 0
        dp_loss_2a3b = 0
        dp_loss_3c2d = 0
        dp_loss_2d1d = 0
        dp_loss_1d0d = 0
        dp_loss_4d0d = 0
        dp_loss_5d4d = 0
        dp_loss_6c5d = 0
        dp_loss_5a6b = 0
        dp_loss_4a5a = 0
        dp_loss_0c4a = 0
        g_0c1a_max = g_0b0c
        g_0c1a_min = 0

        while abs(dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d + dp_loss_1d0d - dp_loss_4d0d - dp_loss_5d4d - dp_loss_6c5d - dp_loss_5a6b - dp_loss_4a5a - dp_loss_0c4a) > 0.1:
            g_0c1a = (g_0c1a_max + g_0c1a_min) / 2
            dp_loss_0c1a = - 1.1 * g_0c1a ** 2
            g_0c4a = g_0b0c - g_0c1a
            dp_loss_1a2a = 5
            dp_loss_2a3b = 0
            dp_loss_3c2d = 0
            dp_loss_2d1d = 0
            dp_loss_1c1d = 0
            dp_loss_1a1b = 0

            g_1a2a_max = g_0c1a
            g_1a2a_min = 0

            cnt3 = 0
            while abs(dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d - dp_loss_1c1d - dp_loss_1a1b) > 0.1:
                g_1a2a = (g_1a2a_max + g_1a2a_min) / 2
                dp_loss_1a2a = - 1.5 * g_1a2a ** 2

                g_2a3b_max = g_1a2a
                g_2a3b_min = 0

                cnt4 = 0

                dp_loss_2a3b = 5
                dp_loss_3c2d = 0
                dp_loss_2c2d = 0
                dp_loss_2a2b = 0
                while abs(dp_loss_2a3b + dp_loss_3c2d - dp_loss_2c2d - dp_loss_2a2b) > 0.1:
                    g_2a3b = (g_2a3b_max + g_2a3b_min) / 2
                    dp_loss_2a3b = - 1.5 * g_2a3b ** 2
                    p3 = p0 + dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b
                    g_draft3 = (abs(p3 - p0) / 100) ** 0.5 * (p3 - p0) / abs(p3 - p0)  # すき間風が部屋から出ていく方を流量正とする
                    g_3c2d = g_2a3b - g_draft3
                    if g_3c2d < 0:
                        g_3c2d = 0
                    dp_loss_3c2d = - 1.5 * g_3c2d ** 2
                    g_2a2b = g_1a2a - g_2a3b
                    p2 = p0 + dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a2b
                    g_draft2 = (abs(p2 - p0) / 100) ** 0.5 * (p2 - p0) / abs(p2 - p0)  # すき間風が部屋から出ていく方を流量正とする
                    g_2c2d = g_2a2b - g_draft2
                    if g_2c2d < 0:
                        g_2c2d = 0
                    dp_loss_2c2d = - 1.5 * g_2c2d ** 2
                    g_2d1d = g_2c2d + g_3c2d
                    g_4a5a_max = g_0b0c - g_0c1a
                    g_4a5a_min = 0

                    dp_loss_4a5a = 5
                    dp_loss_5a6b = 0
                    dp_loss_6c5d = 0
                    dp_loss_5d4d = 0
                    dp_loss_4c4d = 0
                    dp_loss_4a4b = 0

                    cnt5 = 0
                    while abs(dp_loss_4a5a + dp_loss_5a6b + dp_loss_6c5d + dp_loss_5d4d - dp_loss_4c4d - dp_loss_4a4b) > 0.1:
                        g_4a5a = (g_4a5a_max + g_4a5a_min) / 2
                        dp_loss_4a5a = - 1.5 * g_4a5a ** 2

                        g_5a6b_max = g_4a5a
                        g_5a6b_min = 0

                        cnt6 = 0

                        dp_loss_5a6b = 5
                        dp_loss_6c5d = 0
                        dp_loss_5c5d = 0
                        dp_loss_5a5b = 0
                        while abs(dp_loss_5a6b + dp_loss_6c5d - dp_loss_5c5d - dp_loss_5a5b) > 0.1:
                            g_5a6b = (g_5a6b_max + g_5a6b_min) / 2
                            dp_loss_5a6b = - 1.5 * g_5a6b ** 2
                            p6 = p0 + dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c4a + dp_loss_4a5a + dp_loss_5a6b
                            g_draft6 = (abs(p6 - p0) / 100) ** 0.5 * (p6 - p0) / abs(p6 - p0)  # すき間風が部屋から出ていく方を流量正とする
                            g_6c5d = g_5a6b - g_draft6
                            if g_6c5d < 0:
                                g_6c5d = 0
                            dp_loss_6c5d = - 1.5 * g_6c5d ** 2
                            g_5a5b = g_4a5a - g_5a6b
                            p5 = p0 + dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c4a + dp_loss_4a5a + dp_loss_5a5b
                            g_draft5 = (abs(p5 - p0) / 100) ** 0.5 * (p5 - p0) / abs(p5 - p0)  # すき間風が部屋から出ていく方を流量正とする
                            g_5c5d = g_5a5b - g_draft5
                            if g_5c5d < 0:
                                g_5c5d = 0
                            dp_loss_5c5d = - 1.5 * g_5c5d ** 2
                            g_5d4d = g_6c5d + g_5c5d
                            if dp_loss_5a6b + dp_loss_6c5d - dp_loss_5c5d - dp_loss_5a5b > 0:
                                g_5a6b_min = g_5a5b
                            else:
                                g_5a6b_max = g_5a5b

                            cnt6 += 1
                            if cnt6 > 200:
                                break
                        p4 = p0 + dp_loss_0a0b + dp_fan1 + + dp_loss_0b0c + dp_loss_0c4a + dp_loss_4a4b
                        g_draft4 = (abs(p4 - p0) / 100) ** 0.5 * (p4 - p0) / abs(p4 - p0)  # すき間風が部屋から出ていく方を流量正とする
                        g_4a4b = g_0c4a - g_4a5a
                        g_4c4d = g_4a4b - g_draft4
                        g_4d0d = g_4c4d + g_5d4d
                        if g_4c4d < 0:
                            g_4c4d = 0
                        dp_loss_4c4d = - 1.5 * g_4c4d ** 2

                        if dp_loss_4a5a + dp_loss_5a6b + dp_loss_6c5d + dp_loss_5d4d - dp_loss_4c4d - dp_loss_4a4b > 0:
                            g_4a5a_min = g_4a5a
                        else:
                            g_4a5a_max = g_4a5a

                        cnt5 += 1
                        if cnt5 > 200:
                            break

                    if dp_loss_2a3b + dp_loss_3c2d - dp_loss_2c2d - dp_loss_2a2b > 0:
                        g_2a3b_min = g_2a3b
                    else:
                        g_2a3b_max = g_2a3b
                    cnt4 += 1
                    if cnt4 > 200:
                        break

                p1 = p0 + dp_loss_0a0b + dp_fan1 + dp_loss_0c1a + dp_loss_1a1b
                g_draft1 = (abs(p1 - p0) / 100) ** 0.5 * (p1 - p0) / abs(p1 - p0)  # すき間風が部屋から出ていく方を流量正とする
                g_1a1b = g_0c1a - g_1a2a
                g_1c1d = g_1a1b - g_draft1
                g_1d0d = g_1c1d + g_2d1d

                if dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d - dp_loss_1c1d - dp_loss_1a1b > 0:
                    g_1a2a_min = g_1a2a
                else:
                    g_1a2a_max = g_1a2a
                cnt3 += 1
                if cnt3 > 200:
                    break


            # [g_1a2a, g_1d0d, p1, p2, p3, c1, c2, dp_c1] = two_room(g_0c1a, dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c1a)
            #
            # g_0c4a = g_0b0c - g_0c1a
            # dp_loss_0c4a = - 1.1 * g_0c4a ** 2
            # [g_4a5a, g_4d0d, p4, p5, p6, c11, c22, dp_c2] = two_room(dp_loss_0c4a, dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c4a)

            if dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d + dp_loss_1d0d - dp_loss_4d0d - dp_loss_5d4d - dp_loss_6c5d - dp_loss_5a6b - dp_loss_4a5a - dp_loss_0c4a > 0:
                g_0c1a_min = g_0c1a
            else:
                g_0c1a_max = g_0c1a

                cnt2 += 1
                if cnt2 > 200:
                    break

        # while abs(dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d - dp_loss_1c1d - dp_loss_1a1b) > 0.001:
        #     g_0c1a = (g_0c1a_max + g_0c1a_min) / 2
        #     dp_loss_0c1a = - 1.5 * g_0c1a ** 2
        #
        #     # g_1a2a_max = g_0c1a
        #     # g_1a2a_min = 0
        #
        #     dp_loss_o1a = dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c1a
        #     [g_1a2a, g_1d0d, p11, p12, p13, c11, c12, dp_loss_c] = two_room(g_0c1a, dp_loss_o1a)
        #     dp_loss_1d0d = - 1.5 * g_1d0d ** 2
        #
        #     g_4a5a_max = g_0b0c - g_0c1a
        #     g_4a5a_min = 0
        #     dp_loss_4d0d = 0
        #     dp_loss_5d4d = 0
        #     dp_loss_6c5d = 0
        #     dp_loss_5a6b = 0
        #     dp_loss_4a5a = 0
        #     dp_loss_0c4a = 0
        #     cnt3 = 0
        #     while abs(dp_loss_0c1a + dp_loss_c + dp_loss_1d0d - dp_loss_4d0d - dp_loss_5d4d - dp_loss_6c5d - dp_loss_5a6b - dp_loss_4a5a - dp_loss_0c4a) > 0.001:
        #         g_4a5a = (g_4a5a_max + g_4a5a_min) / 2
        #         dp_loss_4a5a = - 1.5 * g_4a5a ** 2
        #
        #         dp_loss_5a6b = 5
        #         dp_loss_6c5d = 0
        #         dp_loss_5c5d = 0
        #         dp_loss_5a5b = 0
        #
        #         g_5a6b_max = g_4a5a
        #         g_5a6b_min = 0
        #         cnt4 = 0
        #
        #         while abs(dp_loss_5a6b + dp_loss_6c5d - dp_loss_5c5d - dp_loss_5a5b) > 0.001:
        #             g_5a6b = (g_5a6b_min + g_5a6b_min ) / 2
        #             dp_loss_5a6b = - 1.5 * g_5a6b ** 2
        #             p6 = p0 + dp_loss_0a0b + dp_loss_0b0c + dp_loss_0c4a + dp_loss_4a5a + dp_loss_5a6b
        #             g_draft6 = (abs(p6 - p0) / 100) ** 0.5 * (p6 - p0) / abs(p6 - p0)  # すき間風が部屋から出ていく方を流量正とする
        #             g_6c5d = g_5a6b - g_draft6
        #             if g_6c5d < 0:
        #                 g_6c5d = 0
        #             dp_loss_6c5d = - 1.5 * g_6c5d ** 2
        #             g_5a5b = g_4a5a - g_6c5d
        #             dp_loss_5a5b = - 1.5 * g_5a5b ** 2
        #             p5 = p0 + dp_loss_0a0b + dp_loss_0b0c + dp_loss_0c4a + dp_loss_4a5a + dp_loss_5a5b
        #             g_draft5 = (abs(p5 - p0) / 100) ** 0.5 * (p5 - p0) / abs(p5 - p0)  # すき間風が部屋から出ていく方を流量正とする
        #             g_5c5d = g_5a5b - g_draft5
        #             g_5d4d = g_5c5d + g_6c5d
        #             if g_5c5d < 0:
        #                 g_5c5d = 0
        #             dp_loss_5c5d = - 1.5 * dp_loss_5c5d ** 2
        #
        #             if dp_loss_5a6b + dp_loss_6c5d - dp_loss_5c5d - dp_loss_5a5b > 0:
        #                 g_5a6b_min = g_5a6b
        #             else:
        #                 g_5a6b_max = g_5a6b
        #
        #             cnt4 += 1
        #             if cnt4 > 50:
        #                 break
        #
        #         g_4a4b = g_0c4a - g_4a5a
        #         dp_loss_4a4b = - 1.5 * g_4a4b ** 2
        #         p4 = p0 + dp_loss_0a0b + dp_loss_0b0c + dp_loss_0c4a + dp_loss_4a4b
        #         g_draft4 = (abs(p4 - p0) / 100) ** 0.5 * (p4 - p0) / abs(p4 - p0)  # すき間風が部屋から出ていく方を流量正とする
        #         g_4c4d = g_4a4b - g_draft4
        #         g_4d0d = g_4c4d + g_5d4d
        #         dp_loss_4d0d = - 1.5 * g_4d0d ** 2
        #
        #         if dp_loss_0c1a + dp_loss_c + dp_loss_1d0d - dp_loss_4d0d - dp_loss_5d4d - dp_loss_6c5d - dp_loss_5a6b - dp_loss_4a5a - dp_loss_0c4a > 0:
        #             g_4a5a_min = g_4a5a
        #         else:
        #             g_4a5a_max = g_4a5a
        #         cnt3 += 1
        #         if cnt3 > 50:
        #             break
        #
        #     if dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d - dp_loss_1c1d - dp_loss_1a1b > 0:
        #         g_0c1a_min = g_0c1a
        #     else:
        #         g_0c1a_max = g_0c1a
        #     cnt2 += 1
        #     if cnt2 > 50:
        #         break
        #
        # #
        # #     # g_0c4a = g_0b0c - g_0c1a
        # #     # dp_loss_0c4a = - 1.5 * g_0c4a ** 2
        # #     # dp_loss_o4a = dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c4a
        # #     # [g_4a5a, g_4d0d, p21, p22, p23, c21, c22, g_5a6b] = two_room(g_0c4a, dp_loss_o4a)
        # #     # dp_loss_4d0d = - 1.5 * g_4d0d ** 2
        # #
        # #     dp_loss_4d0d = 0
        # #     dp_loss_5d4d = 0
        # #     dp_loss_6c5d = 0
        # #     dp_loss_5a6b = 0
        # #     dp_loss_4a5a = 0
        # #     dp_loss_0c4a = 0
        # #
        # #     g_0c4a = g_0b0c - g_0c1a
        # #     dp_loss_0c4a = - 1.5 * g_0c4a ** 2
        # #     g_4a5a_max = g_0c4a
        # #     g_4a5a_min = 0
        # #     while abs(dp_loss_c1 - dp_loss_4d0d - dp_loss_5d4d - dp_loss_6c5d - dp_loss_5a6b - dp_loss_4a5a - dp_loss_0c4a) > 0.001:
        # #         g_4a5a = (g_4a5a_max + g_4a5a_min) / 2
        # #         dp_loss_4a5a = - 1.5 * g_4a5a ** 2
        # #
        # #
        # #
        # #     if dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d - dp_loss_1c1d - dp_loss_1a1b > 0:
        # #         g_0c1a_min = g_0c1a
        # #     else:
        # #         g_0c1a_max = g_0c1a
        # #
        # #     cnt2 += 1
        # #     if cnt2 > 50:
        # #         break

        g_0d0e = g_1d0d + g_4d0d
        dp_loss_0d0e = - 1.1 * g_0d0e ** 2
        dp_fan2 = 150 - 0.1 * g_0d0e ** 2
        g_0e0b = g_0b0c - g_0a0b
        dp_loss_0e0b = - 1.5 * g_0e0b ** 2

        if dp_fan1 + dp_loss_0b0c + dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d + dp_loss_1d0d + dp_fan2 + dp_loss_0d0e + dp_loss_0e0b > 0:
            g_0b0c_min = g_0b0c
        else:
            g_0b0c_max = g_0b0c

        cnt1 += 1
        if cnt1 > 200:
            break

    g_0e0f = g_0d0e - g_0e0b
    dp_loss_0e0f = - 0.1 * g_0e0f ** 2
    if dp_loss_0a0b + dp_fan1 + dp_loss_0b0c + dp_loss_0c1a + dp_loss_1a2a + dp_loss_2a3b + dp_loss_3c2d + dp_loss_2d1d + dp_loss_1d0d + dp_fan2 + dp_loss_0d0e + dp_loss_0e0f > 0:
        g_0a0b_min = g_0a0b
    else:
        g_0a0b_max = g_0a0b

    cnt0 += 1
    if cnt0 > 200:
        break


print(g_0a0b, g_0b0c, g_0c1a, g_1a2a, g_2a3b, g_0c4a, g_4a5a, g_5a6b)
print(p1, p2, p3, p4, p5, p6)
print(cnt0, cnt1, cnt2, cnt3, cnt4, cnt5, cnt6)

print(time.time() - s)
#print(c1, c2, c11,c22)



# 0.684032241420318 0.39940631862510667 0.3848622204078797
# 148.09001073025044 117.25254073576602 116.11189286972834
# 10.056304931640625 23.28071532829199 10.910881514752568 4.884723871503301
# 17 18 17 14
# 23.28071532829199 31.48873187279213
# 10.910881514752568 10.126612975719581 148.09001073025044 117.25254073576602 116.11189286972834 from original
# (10.910881514752568, 10.126612975719581, 148.09001073025047, 117.25254073576605, 116.11189286972836) from this one
