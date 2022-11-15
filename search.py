
import os
import glob
from whoosh.fields import *
from whoosh.index import *
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer
import chardet
import sys
import docx2txt
from win32com import client as wc

# build index for specified folder
def buildIndex(wrkdir):
    if not os.path.exists(wrkdir):
        print('the folder %s does not exist' % wrkdir)
        return

    schema = Schema(title = TEXT(stored=True,analyzer=ChineseAnalyzer()),\
        content = TEXT(analyzer=ChineseAnalyzer()),file_path = ID(stored=True,unique=True))
    
    ix = create_in('myindex',schema, indexname='svn_index')
    w = ix.writer()
    for fil in glob.glob(wrkdir+'/**',recursive=True):
        fil_title = fil.split('\\')[-1]
        try:
            fil_title = fil_title[:fil_title.index('.')]
        except ValueError:
            pass
        
        #process txt documents
        if os.path.isfile(fil) and os.path.splitext(fil)[1] in('.txt','.sql','.csv') \
            and os.stat(fil).st_size<30000:
            ontext_encode = 'utf-8'
            with open(fil,'rb') as f:
                byte_context = f.read()
                context_encode = chardet.detect(byte_context)['encoding']
            with open(fil, encoding=context_encode) as f:
                try:
                    file_content = f.read()
                except UnicodeDecodeError as e:
                    # print(e,f.name)
                    file_content = ''
        else:
            file_content = ''

        #process docx files
        if os.path.isfile(fil) and os.path.splitext(fil)[1] in('.docx') \
            and not fil_title.startswith('~$'):
            try:
                file_content = docx2txt.process(fil)
            except Exception as e:
                file_content = ''
                # print(e,fil)
        
        #process doc files
        tempdir = make_temp_file(wrkdir)
        if os.path.isfile(fil) and os.path.splitext(fil)[1] in('.doc') \
            and not fil_title.startswith('~$'):
            word = wc.Dispatch('Word.Application')
            doc = word.Documents.Open(fil)
            tmpfile = os.path.splitext(fil)[0] +'.docx'
            doc.SaveAs(tmpfile,12)
            doc.Close()
            word.Quit()
            file_content = docx2txt.process(tmpfile)
        remove_temp_file(tempdir)
                      
        w.add_document(title=fil_title,content = file_content, file_path=os.path.join(fil))
    w.commit()

#define search funciton
def searchFun(keyword):
    # keyword for title / content, deault is contect
    search_field = 'content'
    if keyword.startswith('title='):
        search_field = 'title'
        search_keyword = keyword[6:]
    elif keyword.startswith('content='):
        search_keyword = keyword[8:]
    else:
        search_keyword = keyword

    ix = open_dir('myindex','svn_index')
    schema = Schema(title = TEXT(),content = TEXT(),file_path = ID())
    qp = QueryParser(search_field,schema)
    q = qp.parse(search_keyword)

    print('Search result:\n'+'-'*50)
    with ix.searcher() as searcher:
        results = searcher.search(q)
        for r in results:
            print(r.fields()['file_path'])
    print('-'*50)

def make_temp_file(wrkdir):
    tmpdir = os.path.join(wrkdir,'tempdir')
    wrkdir = tmpdir
    i = 1
    while os.path.exists(tmpdir):
        i += 1
        tmpdir = wrkdir + str(i)
    os.mkdir(tmpdir)
    return tmpdir

def remove_temp_file(wrkdir):
    for f in os.listdir(wrkdir):
        os.remove(os.path.join(wrkdir,f))
    os.rmdir(wrkdir)

if __name__ == '__main__':
    if len(sys.argv) >2 and sys.argv[2] == 'rebuild':
        buildIndex(sys.argv[3]) 
    searchFun(sys.argv[1])
