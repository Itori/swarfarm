# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sw_parser', '0020_auto_20161221_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldbosslog',
            name='battle_key',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='riftdungeonitemdrop',
            name='item',
            field=models.IntegerField(choices=[(0, b'Unknown Scroll'), (1, b'Social Summon'), (2, b'Mystical Scroll'), (3, b'Mystical Summon (Crystals)'), (4, b'Fire Scroll'), (5, b'Water Scroll'), (6, b'Wind Scroll'), (7, b'Scroll of Light and Dark'), (8, b'Legendary Scroll'), (9, b'Exclusive Summon (Stones)'), (10, b'Light and Dark Pieces'), (11, b'Legendary Pieces'), (12, b'Transcendance Scroll'), (102, b'Shapeshifting Stone'), (103, b'Power Stone'), (104, b'Summoning Pieces'), (105, b'Secret Dungeon'), (110, b'Low Magic Essence'), (111, b'Mid Magic Essence'), (112, b'High Magic Essence'), (113, b'Low Fire Essence'), (114, b'Mid Fire Essence'), (115, b'High Fire Essence'), (116, b'Low Water Essence'), (117, b'Mid Water Essence'), (118, b'High Water Essence'), (119, b'Low Wind Essence'), (120, b'Mid Wind Essence'), (121, b'High Wind Essence'), (122, b'Low Light Essence'), (123, b'Mid Light Essence'), (124, b'High Light Essence'), (125, b'Low Dark Essence'), (126, b'Mid Dark Essence'), (127, b'High Dark Essence'), (128, b'Hard Wood'), (129, b'Tough Leather'), (130, b'Solid Rock'), (131, b'Solid Iron Ore'), (132, b'Shining Mithril'), (133, b'Thick Cloth'), (134, b'Rune Piece'), (135, b'Magic Dust'), (136, b'Symbol of Harmony'), (137, b'Symbol of Transcendance'), (138, b'Symbol of Chaos'), (139, b'Frozen Water Crystal'), (140, b'Flaming Fire Crystal'), (141, b'Whirling Wind Crystal'), (142, b'Shiny Light Crystal'), (143, b'Pitch-black Dark Crystal'), (144, b'Condensed Magic Crystal'), (145, b'Pure Magic Crystal'), (146, b'Mana'), (147, b'Crystals'), (148, b'Glory Points'), (149, b'Guild Points'), (150, b'Real Money')]),
        ),
        migrations.AlterField(
            model_name='runlog',
            name='drop_type',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown Scroll'), (1, b'Social Summon'), (2, b'Mystical Scroll'), (3, b'Mystical Summon (Crystals)'), (4, b'Fire Scroll'), (5, b'Water Scroll'), (6, b'Wind Scroll'), (7, b'Scroll of Light and Dark'), (8, b'Legendary Scroll'), (9, b'Exclusive Summon (Stones)'), (10, b'Light and Dark Pieces'), (11, b'Legendary Pieces'), (12, b'Transcendance Scroll'), (100, b'Monster'), (101, b'Rune'), (102, b'Shapeshifting Stone'), (103, b'Power Stone'), (104, b'Summoning Pieces'), (105, b'Secret Dungeon'), (110, b'Low Magic Essence'), (111, b'Mid Magic Essence'), (112, b'High Magic Essence'), (113, b'Low Fire Essence'), (114, b'Mid Fire Essence'), (115, b'High Fire Essence'), (116, b'Low Water Essence'), (117, b'Mid Water Essence'), (118, b'High Water Essence'), (119, b'Low Wind Essence'), (120, b'Mid Wind Essence'), (121, b'High Wind Essence'), (122, b'Low Light Essence'), (123, b'Mid Light Essence'), (124, b'High Light Essence'), (125, b'Low Dark Essence'), (126, b'Mid Dark Essence'), (127, b'High Dark Essence'), (128, b'Hard Wood'), (129, b'Tough Leather'), (130, b'Solid Rock'), (131, b'Solid Iron Ore'), (132, b'Shining Mithril'), (133, b'Thick Cloth'), (134, b'Rune Piece'), (135, b'Magic Dust'), (136, b'Symbol of Harmony'), (137, b'Symbol of Transcendance'), (138, b'Symbol of Chaos'), (139, b'Frozen Water Crystal'), (140, b'Flaming Fire Crystal'), (141, b'Whirling Wind Crystal'), (142, b'Shiny Light Crystal'), (143, b'Pitch-black Dark Crystal'), (144, b'Condensed Magic Crystal'), (145, b'Pure Magic Crystal')]),
        ),
        migrations.AlterField(
            model_name='shoprefreshitem',
            name='item',
            field=models.IntegerField(choices=[(0, b'Unknown Scroll'), (1, b'Social Summon'), (2, b'Mystical Scroll'), (3, b'Mystical Summon (Crystals)'), (4, b'Fire Scroll'), (5, b'Water Scroll'), (6, b'Wind Scroll'), (7, b'Scroll of Light and Dark'), (8, b'Legendary Scroll'), (9, b'Exclusive Summon (Stones)'), (10, b'Light and Dark Pieces'), (11, b'Legendary Pieces'), (12, b'Transcendance Scroll'), (102, b'Shapeshifting Stone'), (103, b'Power Stone'), (104, b'Summoning Pieces'), (105, b'Secret Dungeon'), (110, b'Low Magic Essence'), (111, b'Mid Magic Essence'), (112, b'High Magic Essence'), (113, b'Low Fire Essence'), (114, b'Mid Fire Essence'), (115, b'High Fire Essence'), (116, b'Low Water Essence'), (117, b'Mid Water Essence'), (118, b'High Water Essence'), (119, b'Low Wind Essence'), (120, b'Mid Wind Essence'), (121, b'High Wind Essence'), (122, b'Low Light Essence'), (123, b'Mid Light Essence'), (124, b'High Light Essence'), (125, b'Low Dark Essence'), (126, b'Mid Dark Essence'), (127, b'High Dark Essence'), (128, b'Hard Wood'), (129, b'Tough Leather'), (130, b'Solid Rock'), (131, b'Solid Iron Ore'), (132, b'Shining Mithril'), (133, b'Thick Cloth'), (134, b'Rune Piece'), (135, b'Magic Dust'), (136, b'Symbol of Harmony'), (137, b'Symbol of Transcendance'), (138, b'Symbol of Chaos'), (139, b'Frozen Water Crystal'), (140, b'Flaming Fire Crystal'), (141, b'Whirling Wind Crystal'), (142, b'Shiny Light Crystal'), (143, b'Pitch-black Dark Crystal'), (144, b'Condensed Magic Crystal'), (145, b'Pure Magic Crystal'), (146, b'Mana'), (147, b'Crystals'), (148, b'Glory Points'), (149, b'Guild Points'), (150, b'Real Money')]),
        ),
        migrations.AlterField(
            model_name='summonlog',
            name='summon_method',
            field=models.IntegerField(choices=[(0, b'Unknown Scroll'), (1, b'Social Summon'), (2, b'Mystical Scroll'), (3, b'Mystical Summon (Crystals)'), (4, b'Fire Scroll'), (5, b'Water Scroll'), (6, b'Wind Scroll'), (7, b'Scroll of Light and Dark'), (8, b'Legendary Scroll'), (9, b'Exclusive Summon (Stones)'), (10, b'Light and Dark Pieces'), (11, b'Legendary Pieces'), (12, b'Transcendance Scroll')]),
        ),
        migrations.AlterField(
            model_name='worldbossitemdrop',
            name='item',
            field=models.IntegerField(choices=[(0, b'Unknown Scroll'), (1, b'Social Summon'), (2, b'Mystical Scroll'), (3, b'Mystical Summon (Crystals)'), (4, b'Fire Scroll'), (5, b'Water Scroll'), (6, b'Wind Scroll'), (7, b'Scroll of Light and Dark'), (8, b'Legendary Scroll'), (9, b'Exclusive Summon (Stones)'), (10, b'Light and Dark Pieces'), (11, b'Legendary Pieces'), (12, b'Transcendance Scroll'), (102, b'Shapeshifting Stone'), (103, b'Power Stone'), (104, b'Summoning Pieces'), (105, b'Secret Dungeon'), (110, b'Low Magic Essence'), (111, b'Mid Magic Essence'), (112, b'High Magic Essence'), (113, b'Low Fire Essence'), (114, b'Mid Fire Essence'), (115, b'High Fire Essence'), (116, b'Low Water Essence'), (117, b'Mid Water Essence'), (118, b'High Water Essence'), (119, b'Low Wind Essence'), (120, b'Mid Wind Essence'), (121, b'High Wind Essence'), (122, b'Low Light Essence'), (123, b'Mid Light Essence'), (124, b'High Light Essence'), (125, b'Low Dark Essence'), (126, b'Mid Dark Essence'), (127, b'High Dark Essence'), (128, b'Hard Wood'), (129, b'Tough Leather'), (130, b'Solid Rock'), (131, b'Solid Iron Ore'), (132, b'Shining Mithril'), (133, b'Thick Cloth'), (134, b'Rune Piece'), (135, b'Magic Dust'), (136, b'Symbol of Harmony'), (137, b'Symbol of Transcendance'), (138, b'Symbol of Chaos'), (139, b'Frozen Water Crystal'), (140, b'Flaming Fire Crystal'), (141, b'Whirling Wind Crystal'), (142, b'Shiny Light Crystal'), (143, b'Pitch-black Dark Crystal'), (144, b'Condensed Magic Crystal'), (145, b'Pure Magic Crystal'), (146, b'Mana'), (147, b'Crystals'), (148, b'Glory Points'), (149, b'Guild Points'), (150, b'Real Money')]),
        ),
    ]
