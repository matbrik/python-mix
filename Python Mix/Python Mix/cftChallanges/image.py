import os


filenames = ['ipp',
'ipp(1)',
'ipp(2)',
'ipp(3)',
'ipp(4)',
'ipp(5)',
'ipp(6)',
'ipp(7)',
'ipp(8)',
'ipp(9)',
'ipp(10)',
'ipp(11)',
'ipp(12)',
'ipp(13)',
'ipp(14)',
'ipp(15)',
'ipp(16)',
'ipp(17)',
'ipp(18)',
'ipp(19)',
'ipp(20)',
'ipp(21)',
'ipp(22)',
'ipp(23)',
'ipp(24)',
'ipp(25)',
'ipp(26)',
'ipp(27)',
'ipp(28)',
'ipp(29)',
'ipp(30)',
'ipp(31)',
'ipp(32)',
'ipp(33)',
'ipp(34)',
'ipp(35)',
'ipp(36)',
'ipp(37)',
'ipp(38)',
'ipp(39)',
'ipp(40)',
'ipp(41)',
'ipp(42)',
'ipp(43)',
'ipp(44)',
'ipp(45)',
'ipp(46)',
'ipp(47)',
'ipp(48)',
'ipp(49)',
'ipp(50)',
'ipp(51)',
'ipp(52)',
'ipp(53)',
'ipp(54)',
'ipp(55)',
'ipp(56)',
'ipp(57)',
'ipp(58)',
'ipp(59)',
'ipp(60)',
'ipp(61)',
'ipp(62)',
'ipp(63)',
'ipp(64)',
'ipp(65)',
'ipp(66)',
'ipp(67)',
'ipp(68)',
'ipp(69)',
'ipp(70)',
'ipp(71)',
'ipp(72)',
'ipp(73)',
'ipp(74)',
'ipp(75)',
'ipp(76)',
'ipp(77)',
'ipp(78)',
'ipp(79)',
'ipp(80)',
'ipp(81)',
'ipp(82)',
'ipp(83)',
'ipp(84)',
'ipp(85)',
'ipp(86)',
'ipp(87)',
'ipp(88)',
'ipp(89)',
'ipp(90)',
'ipp(91)',
'ipp(92)',
'ipp(93)',
'ipp(94)',
'ipp(95)',
'ipp(96)',
'ipp(97)',
'ipp(98)',
'ipp(99)',
'ipp(100)',
'ipp(101)',
'ipp(102)',
'ipp(103)',
'ipp(104)',
'ipp(105)',
'ipp(106)',
'ipp(107)',
'ipp(108)',
'ipp(109)',
'ipp(110)',
'ipp(111)',
'ipp(112)',
'ipp(113)',
'ipp(114)',
'ipp(115)',
'ipp(116)',
'ipp(117)',
'ipp(118)',
'ipp(119)',
'ipp(120)',
'ipp(121)',
'ipp(122)',
'ipp(123)',
'ipp(124)',
'ipp(125)',
'ipp(126)',
'ipp(127)',
'ipp(128)',
'ipp(129)',
'ipp(130)',
'ipp(131)',
'ipp(132)',
'ipp(133)',
'ipp(134)',
'ipp(135)',
'ipp(136)',
'ipp(137)',
'ipp(138)',
'ipp(139)',
'ipp(140)',
'ipp(141)',
'ipp(142)',
'ipp(143)',
'ipp(144)',
'ipp(145)',
'ipp(146)',
'ipp(147)',
'ipp(148)',
'ipp(149)',
'ipp(150)',
'ipp(151)',
'ipp(152)',
'ipp(153)',
'ipp(154)',
'ipp(155)',
'ipp(156)',
'ipp(157)',
'ipp(158)',
'ipp(159)',
'ipp(160)',
'ipp(161)',
'ipp(162)',
'ipp(163)',
'ipp(164)',
'ipp(165)',
'ipp(166)',
'ipp(167)',
'ipp(168)',
'ipp(169)',
'ipp(170)',
'ipp(171)',
'ipp(172)',
'ipp(173)',
'ipp(174)',
'ipp(175)',
'ipp(176)',
'ipp(177)',
'ipp(178)',
'ipp(179)',
'ipp(180)',
'ipp(181)',
'ipp(182)',
'ipp(183)',
'ipp(184)',
'ipp(185)',
'ipp(186)',
'ipp(187)',
'ipp(188)',
'ipp(189)',
'ipp(190)',
'ipp(191)',
'ipp(192)',
'ipp(193)',
'ipp(194)',
'ipp(195)',
'ipp(196)',
'ipp(197)',
'ipp(198)',
'ipp(199)',
'ipp(200)',
'ipp(201)',
'ipp(202)',
'ipp(203)',
'ipp(204)',
'ipp(205)',
'ipp(206)',
'ipp(207)',
'ipp(208)',
'ipp(209)',
'ipp(210)',
'ipp(211)',
'ipp(212)',
'ipp(213)',
'ipp(214)',
'ipp(215)',
'ipp(216)',
'ipp(217)',
'ipp(218)',
'ipp(219)',
'ipp(220)',
'ipp(221)',
'ipp(222)',
'ipp(223)',
'ipp(224)',
'ipp(225)',
'ipp(226)',
'ipp(227)',
'ipp(228)',
'ipp(229)',
'ipp(230)',
'ipp(231)',
'ipp(232)',
'ipp(233)',
'ipp(234)',
'ipp(235)',
'ipp(236)',
'ipp(237)',
'ipp(238)',
'ipp(239)',
'ipp(240)',
'ipp(241)',
'ipp(242)',
'ipp(243)',
'ipp(244)',
'ipp(245)',
'ipp(246)',
'ipp(247)',
'ipp(248)',
'ipp(249)',
'ipp(250)',
'ipp(251)',
'ipp(252)',
'ipp(253)',
'ipp(254)',
'ipp(255)',
'ipp(256)',
'ipp(257)',
'ipp(258)',
'ipp(259)',
'ipp(260)',
'ipp(261)',
'ipp(262)',
'ipp(263)',
'ipp(264)',
'ipp(265)',
'ipp(266)',
'ipp(267)',
'ipp(268)',
'ipp(269)',
'ipp(270)',
'ipp(271)',
'ipp(272)',
'ipp(273)',
'ipp(274)',
'ipp(275)',
'ipp(276)',
'ipp(277)',
'ipp(278)',
'ipp(279)',
'ipp(280)',
'ipp(281)',
'ipp(282)',
'ipp(283)',
'ipp(284)',
'ipp(285)']
with open('path/to/output/file', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)