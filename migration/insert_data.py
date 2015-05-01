# -*- coding: utf-8 -*-

import sys
import sqlite3 as lite
from datetime import datetime

from lxml import etree


def parse_file(dname):
    fname = "data/{0}.xml.new.xml".format(dname)
    return etree.parse(fname)


def store_data(conn, query, data):
    conn.executemany(query, data)
    conn.rollback()


def get_int_value(parent, node_name):
    n = parent.find(node_name)
    if n is not None:
        return int(n.text)
    return None


def get_node_value(parent, node_name):
    n = parent.find(node_name)
    if n is not None:
        return n.text
    return ''


def get_datetime_value(parent, node_name):
    n = parent.find(node_name)
    if n is not None:
        return datetime.strptime(n.text, "%Y-%m-%dT%H:%M:%S")
    return None



def load_docname(conn):
    t_query = "insert into documents_docname(id, docname) values (?, ?);"
    tree = parse_file("DOCNAME")
    data = []
    for dnm in tree.findall("DOCNAME"):
        data.append((
            int(dnm.find("ID_DOCNAME").text),
            dnm.find("DocName").text
        ))
    store_data(conn, t_query, data)


def load_languages(conn):
    t_query = "insert into documents_languages(id, language) values(?, ?);"
    tree = parse_file("Languages")
    data = []
    for lng in tree.findall("Languages"):
        data.append((
            int(lng.find(u"Код").text),
            lng.find(u"Язык").text
        ))
    store_data(conn, t_query, data)


def load_typedoc(conn):
    t_query = "insert into documents_typedoc(doctype) values(?);"
    tree = parse_file("TypeDoc")
    data = []
    for lng in tree.findall("TypeDoc"):
        data.append((
            lng.find("Type").text
        ))
    store_data(conn, t_query, data)


def load_reference(conn):
    t_query = "insert into documents_reference(id, ACnumber, notes, page, name_id) values(?, ?, ?, ?, ?);"
    tree = parse_file("Ссылки")
    data = []
    for lng in tree.findall(u"Ссылки"):
        data.append((
            int(lng.find(u"Код1").text),
            lng.find(u"НомерАС").text,
            get_node_value(lng, u"Примечания"),
            get_node_value(lng, u"Стр"),
            int(lng.find(u"Имена_Код").text)

        ))
    store_data(conn, t_query, data)


def load_category(conn):
    t_query = "insert into documents_category(id, parent_code_id, level, name, path) values(?, ?, ?, ?, ?);"
    tree = parse_file("Категории")
    data = []
    for lng in tree.findall(u"Категории"):
        data.append((
            int(lng.find(u"Код_категории").text),
            int(lng.find(u"Код_родительской_категории").text),
            int(lng.find(u"Уровень").text),
            get_node_value(lng, u"Категория"),
            lng.find("Path").text

        ))
    store_data(conn, t_query, data)


def load_txtcategory(conn):
    t_query = "insert into documents_textcategory(catalog_id, category_id, timestamp) values(?, ?, ?);"
    tree = parse_file("Категоризация текстов")
    data = []
    for lng in tree.findall(u"Категоризация_x0020_текстов"):
        data.append((
            int(lng.find(u"Код_текста").text),
            int(lng.find(u"Код_категории").text),
            get_datetime_value(lng, "TimeStamp"),
        ))
    store_data(conn, t_query, data)


def load_name(conn):
    t_query = "insert into personalies_name(id, name, info) values(?, ?, ?);"
    tree = parse_file("Имена")
    data = []
    for lng in tree.findall(u"Имена"):
        data.append((
            int(lng.find(u"Код1").text),
            lng.find(u"Имя").text,
            # XXX Insert correct field
            '',
        ))
    store_data(conn, t_query, data)


def load_authors(conn):
    t_query = "insert into personalies_author(id, catalog_id, names_code, status, note, operator, date) values(?, ?, ?, ?, ?, ?, ?);"
    tree = parse_file("Авторы")
    data = []
    for lng in tree.findall(u"Авторы"):
        data.append((
            int(lng.find(u"ID_Авторы").text),
            get_int_value(lng, u"Код_каталог"),
            int(lng.find(u"Код_именник").text),
            lng.find(u"Статус").text,
            get_node_value(lng, u"Примечание"),
            get_node_value(lng, u"Оператор"),
            get_datetime_value(lng, u"Дата")
        ))
    store_data(conn, t_query, data)


def load_receiver(conn):
    t_query = "insert into personalies_receiver(id, person, title, 'group', id_doc) values(?, ?, ?, ?, ?);"
    tree = parse_file("Адресат")
    data = []
    for lng in tree.findall(u"Адресат"):
        data.append((
            int(lng.find(u"id_adr").text),
            get_node_value(lng, u"Адресат-персона"),
            get_node_value(lng, u"Адресат-титул"),
            get_node_value(lng, u"Адресат-группа"),
            int(lng.find("id_doc").text)
        ))
    store_data(conn, t_query, data)


def load_wiki(conn):
    t_query = "insert into samizdat_wikitexts values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    tree = parse_file("wiki_texts")
    data = []
    for lng in tree.findall("wiki_texts"):
        data.append((
            get_int_value(lng, "ID_TRUE"),
            get_node_value(lng, "nazv"),
            get_node_value(lng, "red_zag"),
            get_node_value(lng, "avtor"),
            get_node_value(lng, "perevodchik"),
            get_node_value(lng, "redaktor"),
            get_node_value(lng, "data_n"),
            get_node_value(lng, "mesto_n"),
            get_node_value(lng, "data_i"),
            get_node_value(lng, "mesto_i"),
            get_node_value(lng, "zhanr"),
            get_node_value(lng, "picture"),
            get_node_value(lng, "samizdat"),
            get_node_value(lng, "kategorii"),
            get_node_value(lng, "title"),
            get_node_value(lng, "link"),
            get_node_value(lng, "user"),
            get_node_value(lng, "ruwiki"),
            get_node_value(lng, "enwiki"),
            # XXX Get correct field name
            None,
            get_node_value(lng, "oborotka"),
        ))
    store_data(conn, t_query, data)


def load_xtc(conn):
    t_query = "insert into samizdat_xtc values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    tree = parse_file("ХТС")
    data = []
    for lng in tree.findall(u"ХТС"):
        data.append((
            get_int_value(lng, "ID"),
            get_node_value(lng, "Nom"),
            get_node_value(lng, "Pages"),
            get_int_value(lng, "Pages_from"),
            get_int_value(lng, "Pages_to"),
            get_node_value(lng, "Profile"),
            get_node_value(lng, "Notes"),
            get_node_value(lng, "NomDoc"),
            get_node_value(lng, u"Оператор"),
            get_datetime_value(lng, u"Дата_x020_ввода"),
        ))
    store_data(conn, t_query, data)


def load_catalog(conn):
    t_query = "insert into samizdat_catalog values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    tree = parse_file("Каталог")
    data = []
    for lng in tree.findall(u"Каталог"):
        data.append((
            get_int_value(lng, u"Код"),
            get_node_value(lng, u"Язык"),
            get_node_value(lng, u"Автор"),
            get_node_value(lng, u"TypeDoc"),
            get_node_value(lng, u"Название"),
            get_node_value(lng, u"Место"),
            get_node_value(lng, u"PlacePrim"),
            get_node_value(lng, u"Дата"),
            get_node_value(lng, u"DatePrim"),
            get_datetime_value(lng, u"Date1"),
            get_node_value(lng, u"Troubles"),
            get_node_value(lng, u"Hr"),
            get_node_value(lng, u"HrPoisk"),
            get_node_value(lng, u"Ready"),
            get_node_value(lng, u"Художка"),
            get_node_value(lng, u"Ссылка"),
            get_node_value(lng, u"user"),
            get_node_value(lng, u"ruwiki"),
            get_node_value(lng, u"enwiki"),
            get_int_value(lng, "ID_TRUE"),
            get_node_value(lng, u"nazv"),
            get_node_value(lng, u"red_zag"),
            get_node_value(lng, u"avtor"),
            get_node_value(lng, u"perevodchik"),
            get_node_value(lng, u"redaktor"),
            get_node_value(lng, u"data_n"),
            get_node_value(lng, u"mesto_n"),
            get_node_value(lng, u"data_i"),
            get_node_value(lng, u"mesto_i"),
            get_node_value(lng, u"zhanr"),
            get_node_value(lng, u"picture"),
            get_node_value(lng, u"samizdat"),
            get_node_value(lng, u"kategorii"),
            get_node_value(lng, u"title"),
            get_node_value(lng, u"link"),
            get_node_value(lng, u"user"),
            get_node_value(lng, u"ruwiki"),
            get_node_value(lng, "enwiki"),
            # XXX Get correct field name
            None,
            get_node_value(lng, "oborotka"),
        ))
    store_data(conn, t_query, data)
def load_all():
    con = None
    try:
        con = lite.connect("../djamizdat/db.sqlite3")
        load_docname(con)
        load_languages(con)
        # load_typedoc(con)
        load_reference(con)
        load_category(con)
        load_txtcategory(con)
        load_name(con)
        load_authors(con)
        load_receiver(con)
        load_wiki(con)
        load_xtc(con)
    except lite.Error, e:
        print "error:{0}".format(e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    load_all()
