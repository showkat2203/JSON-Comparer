import json
import webbrowser, os, sys
from json2html import *

f = open('output.html', 'w')
black_list = []
txt = ''

def load_json(file_path):
    fh = open(file_path, 'r')
    data = json.load(fh)
    fh.close()

    return data


def main():
    global output

    output = "<html>"
    output += '<head>' \
                '<style></style>' \
              '<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400" rel="stylesheet">' \
              '<link rel="stylesheet" href="base.css">'
    output += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">'
    output += '<meta charset="UTF-8">'
    output += '<title>JSON Comparer</title>'
    output += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>'
    output += '<script src="https://www.gstatic.com/charts/loader.js"></script></head>'
    output += '<body><div class="container"><div class="row"> <div class="col-md-6" row="30" id="original_json"> ' \
              # '<ul>Hello&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sonnet</ul> '

    # import testing JSON files to Python structures
    a_json = load_json('a.json')
    b_json = load_json('b.json')

    a_json = json.dumps(a_json)
    b_json = json.dumps(b_json)

    output += '</div> ' \
              '<div class="col-md-6" id="miss_json">' \
              '</div></div></div></div></body><script> ' \
              'var original_data = ' + a_json + '; var miss_data = ' + b_json + '; var textedJson1 = JSON.stringify(original_data, undefined, 4);' \
              'var textedJson2 = JSON.stringify(miss_data, undefined, 4); '\
              # '$("#original_json").text(textedJson1); '
              # '$("#miss_json").text(textedJson2); '

    output += 'var f = textedJson1.split("\\n"); var g = textedJson2.split("\\n"); ' \
              'var fl = 0, space, split_text ;' \
              'for(var i=0; i<f.length; i++) { split_text = f[i].split(":")[1]; ' \
                   'if( f[i] == g[i] )' \
                    '{'\
                        'if(fl==0) '\
                        '{' \
                                'space = f[i].search(/\S/) ;' \
                                'while(space--) $("#original_json").append("&nbsp;");' \
                                '$("#original_json").append(f[i]);' \
                                '' \
                                'space = g[i].search(/\S/); ' \
                                'while(space--) $("#miss_json").append("&nbsp;");' \
                                '$("#miss_json").append(g[i]);  fl = 1; '\
                        '}'\
                        'else'\
                        '{'\
                                'space = f[i].search(/\S/) ;' \
                                '$("#original_json").append("<br/>");' \
                                'while(space--) $("#original_json").append("&nbsp;");' \
                                '$("#original_json").append(f[i]);' \
                                '' \
                                'space = g[i].search(/\S/) ; ' \
                                '$("#miss_json").append("<br/>");' \
                                'while(space--) $("#miss_json").append("&nbsp;");' \
                                '$("#miss_json").append(g[i]);' \
                        '}'\
                    '}'\
                    'else'\
                    '{' \
                       'if(fl==0) '\
                        '{' \
                                'space = f[i].search(/\S/) ;' \
                                'while(space--) $("#original_json").append("&nbsp;");' \
                                '$("#original_json").append("<span>" + f[i] + "</span>"); fl = 1;' \
                                '' \
                                'space = g[i].search(/\S/) ; ' \
                                'while(space--) $("#miss_json").append("&nbsp;");' \
                                '$("#miss_json").append("<span>" + g[i] + "</span>");' \
                        '}'\
                        'else'\
                        '{'\
                                'space = f[i].search(/\S/) ;' \
                                '$("#original_json").append("<br/>");' \
                                'while(space--) $("#original_json").append("&nbsp;");' \
                                '$("#original_json").append("<span>" + String(f[i]) + "</span>");' \
                                '' \
                                'space = g[i].search(/\S/) ; ' \
                                '$("#miss_json").append("<br/>");' \
                                'while(space--) $("#miss_json").append("&nbsp;");' \
                                '$("#miss_json").append("<span>" + String(g[i]) + "</span>");' \
                        '}'\
                    '}'\
              '}'

    output += "</script></html>"

    f.write(output)
    f.close()
    root_path = sys.path[0]
    webbrowser.open(os.path.join(root_path, 'output.html'))

if (__name__ == '__main__'):
    main()
    # print(output)
