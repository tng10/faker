# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}', '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}', '{{prefix}} {{first_name}} {{last_name}}')

    prefixes_female = (
        "พลเอก", "พลโท", "พลตรี", "พันเอก", "พันโท", "พันตรี", "ร้อยเอก", "ร้อยโท",
        "ร้อยตรี",
        "จ่าสิบเอก", "จ่าสิบโท", "จ่าสิบตรี", "สิบเอก", "สิบโท", "สิบตรี", "พลทหาร",
        "พลเรือเอก", "พลเรือโท", "พลเรือตรี", "นาวาเอก", "นาวาโท", "นาวาตรี", "เรือเอก",
        "เรือโท", "เรือตรี", "พันจ่าเอก", "พันจ่าโท", "พันจ่าตรี", "จ่าเอก", "จ่าโท",
        "จ่าตรี", "พลทหาร", "พลอากาศเอก", "พลอากาศโท", "พลอากาศตรี", "นาวาอากาศเอก",
        "นาวาอากาศโท", "นาวาอากาศตรี", "เรืออากาศเอก", "เรืออากาศโท", "เรืออากาศตรี",
        "พันจ่าอากาศเอก", "พันจ่าอากาศโท", "พันจ่าอากาศตรี", "จ่าอากาศเอก", "จ่าอากาศโท",
        "จ่าอากาศตรี", "พลทหาร", "พลตำรวจเอก", "พลตำรวจโท", "พลตำรวจตรี", "พันตำรวจเอก",
        "พันตำรวจโท", "พันตำรวจตรี", "ร้อยตำรวจเอก", "ร้อยตำรวจโท", "ร้อยตำรวจตรี",
        "นายดาบตำรวจ", "จ่าสิบตำรวจ", "สิบตำรวจเอก", "สิบตำรวจโท", "สิบตำรวจตรี",
        "พลตำรวจ", "นาง", "นางสาว", "หม่อมหลวง", "หม่อมราชวงศ์", "พล.อ.",
        "พล.ท.", "พล.ต.", "พ.อ.", "พ.ท.", "พ.ต.", "ร.อ.", "ร.ท.", "ร.ต.", "จ.ส.อ.",
        "จ.ส.ท.",
        "จ.ส.ต.", "ส.อ.", "ส.ท.", "ส.ต.", "พลฯ", "พล.ร.อ.", "พล.ร.ท.", "พล.ร.ต.", "น.อ.",
        "น.ท.", "น.ต.", "ร.อ.", "ร.ท.", "ร.ต.", "พ.จ.อ.", "พ.จ.ท.", "พ.จ.ต.", "จ.อ.",
        "จ.ท.",
        "จ.ต.", "พลฯ", "พล.อ.อ.", "พล.อ.ท.", "พล.อ.ต.", "น.อ.", "น.ท.", "น.ต.", "ร.อ.",
        "ร.ท.", "ร.ต.", "พ.อ.อ.", "พ.อ.ท.", "พ.อ.ต.", "จ.อ.", "จ.ท.", "จ.ต.", "พลฯ",
        "พล.ต.อ.", "พล.ต.ท.", "พล.ต.ต.", "พ.ต.อ.", "พ.ต.ท.", "พ.ต.ต.", "ร.ต.อ.", "ร.ต.ท.",
        "ร.ต.ต.", "ด.ต.", "จ.ส.ต.", "ส.ต.อ.", "ส.ต.ท.", "ส.ต.ต.", "พลฯ", "ม.ล.", "ม.ร.ว.")
    prefixes_male = (
        "พลเอก", "พลโท", "พลตรี", "พันเอก", "พันโท", "พันตรี", "ร้อยเอก", "ร้อยโท",
        "ร้อยตรี",
        "จ่าสิบเอก", "จ่าสิบโท", "จ่าสิบตรี", "สิบเอก", "สิบโท", "สิบตรี", "พลทหาร",
        "พลเรือเอก", "พลเรือโท", "พลเรือตรี", "นาวาเอก", "นาวาโท", "นาวาตรี", "เรือเอก",
        "เรือโท", "เรือตรี", "พันจ่าเอก", "พันจ่าโท", "พันจ่าตรี", "จ่าเอก", "จ่าโท",
        "จ่าตรี", "พลทหาร", "พลอากาศเอก", "พลอากาศโท", "พลอากาศตรี", "นาวาอากาศเอก",
        "นาวาอากาศโท", "นาวาอากาศตรี", "เรืออากาศเอก", "เรืออากาศโท", "เรืออากาศตรี",
        "พันจ่าอากาศเอก", "พันจ่าอากาศโท", "พันจ่าอากาศตรี", "จ่าอากาศเอก", "จ่าอากาศโท",
        "จ่าอากาศตรี", "พลทหาร", "พลตำรวจเอก", "พลตำรวจโท", "พลตำรวจตรี", "พันตำรวจเอก",
        "พันตำรวจโท", "พันตำรวจตรี", "ร้อยตำรวจเอก", "ร้อยตำรวจโท", "ร้อยตำรวจตรี",
        "นายดาบตำรวจ", "จ่าสิบตำรวจ", "สิบตำรวจเอก", "สิบตำรวจโท", "สิบตำรวจตรี",
        "พลตำรวจ",
        "นาย", "บาทหลวง", "หม่อมหลวง", "หม่อมราชวงศ์", "สามเณร", "พระ",
        "พระอธิการ", "เจ้าอธิการ", "พระปลัด", "พระสมุห์", "พระใบฎีกา", "พระครูปลัด",
        "พระครูสมุห์", "พระครูใบฎีกา", "พระมหา", "พระครูธรรมธร", "พระครูวินัยธร", "พล.อ.",
        "พล.ท.", "พล.ต.", "พ.อ.", "พ.ท.", "พ.ต.", "ร.อ.", "ร.ท.", "ร.ต.", "จ.ส.อ.",
        "จ.ส.ท.",
        "จ.ส.ต.", "ส.อ.", "ส.ท.", "ส.ต.", "พลฯ", "พล.ร.อ.", "พล.ร.ท.", "พล.ร.ต.", "น.อ.",
        "น.ท.", "น.ต.", "ร.อ.", "ร.ท.", "ร.ต.", "พ.จ.อ.", "พ.จ.ท.", "พ.จ.ต.", "จ.อ.",
        "จ.ท.",
        "จ.ต.", "พลฯ", "พล.อ.อ.", "พล.อ.ท.", "พล.อ.ต.", "น.อ.", "น.ท.", "น.ต.", "ร.อ.",
        "ร.ท.", "ร.ต.", "พ.อ.อ.", "พ.อ.ท.", "พ.อ.ต.", "จ.อ.", "จ.ท.", "จ.ต.", "พลฯ",
        "พล.ต.อ.", "พล.ต.ท.", "พล.ต.ต.", "พ.ต.อ.", "พ.ต.ท.", "พ.ต.ต.", "ร.ต.อ.", "ร.ต.ท.",
        "ร.ต.ต.", "ด.ต.", "จ.ส.ต.", "ส.ต.อ.", "ส.ต.ท.", "ส.ต.ต.", "พลฯ", "ม.ล.", "ม.ร.ว.")

    prefixes = prefixes_female + prefixes_male

    first_names = (
        "พรชนก", "พัชชาพลอย", "ภีม", "กชพร", "พัทธพล", "สรัลพร", "จินจุฑา", "สรวุฒิ",
        "สุวกิจ", "พริมา", "ดาริน", "พินท์ธุสร", "กุลนัน", "ณัฐชา", "ณัฐกฤตา", "สิทธิกร",
        "วศิน", "อภิสรา", "ณัฐวรรณ", "ธันรดี", "นิรชา", "ธันยชนก", "กมลชนก", "จารุวรรณ",
        "ผจงรักษ์", "ภัคจิรา", "ปัทธมพร", "สุวิจักษ์", "นพเก้า", "รัชชานนท์", "อธิศ",
        "คุณาพร", "อริสรา", "ทัศวรรณ", "ชัยวัฒน์", "ภัณฑิรา", "ศุภสุตา", "พัชรพร",
        "ภูเบศ",
        "พัทธมน", "ชัญญา", "ปัณณวิชย์", "ชวิน", "ภาดา", "ชนิกานต์", "ณัฐวดี", "ชาลิสา",
        "ประเมศฐ์", "ศุภสิทธิ์", "สิทธิวัต", "ธีธีช", "ญาดา", "เพ็ญพิชชา", "อนนต์",
        "ชายฟ้า",
        "ปวัน", "อัญญาร", "ญานิศา", "ภาคย์", "ชญานินท์", "ชยาภัทร", "จิตริน", "วัศยา",
        "ปิติภัทร", "นิชากานต์", "ปริน", "ธนัชชา",)
    last_names = (
        "ปรัชญาโรจน์", "เทียนวาฤิทธิ์", "บรรเริงศรี", "สุขีนัย",
        "โพชสาลี", "ใช้สถิตย์", "สัจจะบริบูรณ์", "กมลานนท์", "นีรชะพงษ์", "เพียรดวงศรี",
        "ผาสุข", "โล่สถาพรพิพิธ", "สุรประเสริฐ", "ผาตินาวิน", "เชยชื่น", "วสุนันต์",
        "กำสุนทร", "ศรีลีเลิศ", "บุญพึ่งบารมี", "โสรัตนชัย", "เบญจภัทรนนท์", "อินทร์อ่ำ",
        "พิฆาตสิงขร", "ศรีสุนทร", "ผลโพธิ์", "คงชยาสุขวัฒน์", "เจริญสุขโสพล", "บรรลุพงษ์",
        "ชมศรี", "ตังคเสฐกุล", "โขวิฑูนกิต", "ทศพรพิทักษ์กุล", "วิมลโนต", "กิตติคุณ",
        "เมธาวรกุล", "ปิตานุวัฒน์", "ภูศิลารุ่งเรือง", "ตุรงคินานนท์", "ชินะกิจประภา",
        "โพธานันท์", "อยู่ประเสริฐ", "เมธาวรกุล", "เวทยศาสน์", "สุขสว่าง", "อเนกวรกุล",
        "พิชญ์พันธ์เดชา", "สิทธิ์เสาวภาคย์", "สุระประจิต", "คงศรี", "ตรีเกษมมาด",
        "หาบพนม",
        "วรรณไพฑูลศรี", "วิญญูวานิชกุล", "พงศ์พาณิชย์", "เพิ่มชาติ", "ไชยหิรัญการณ์",
        "ธารทนานนท์", "นรมน", "ประยูงหงส์", "เลิศสาธยานุศักดิ์", "ผลอวยพร", "ประคัลภวงศ์",
        "ธิติภัทตรายันยง", "กฤตายานุกุล", "ศิริภัยบูล",)
