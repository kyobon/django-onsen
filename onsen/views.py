from django.shortcuts import render
from django.http import HttpResponse
from .forms import OnsenForm
from .models import Onsen
from django.core.paginator import Paginator

def index(request):
    #初期状態
    inidic = {
        'place':'選択しない',
        'skin':2,
        'efficacy':'選択しない'
    }
    form = OnsenForm(initial=inidic)
    data = []
    #共通処理
    params = {
        'title':'温泉地検索',
        'form':form,
        'data':data,
    }
    return render(request, 'onsen/index.html', params)    

def result(request):
    #URLのクエリーパラメータの辞書を取得
    dic = request.GET
    #フォームの入力値を取得
    place = dic['place']
    skin = dic['skin']
    efficacy = dic['efficacy']
    pag = dic.get(key='pag',default=1)
    #フォームに入力値を代入
    form = OnsenForm(request.GET)
    #条件に合うものを検索
    data = Onsen.objects.filter(place__contains=place,efficacy__contains=efficacy,skin__contains=skin)
    #肌質のパラメータを表示用に変える
    if skin==1:
        vskin = '敏感肌'
    else :
        vskin = '敏感肌ではない'
    #ページネーション
    page = Paginator(data,10)

    #共通処理
    params = {
        'title':'温泉地検索',
        'form':form,
        'data':page.get_page(pag),
        'vplace':place,
        'vskin':vskin,
        'vefficacy':efficacy,
        'skin':skin,
    }
    return render(request, 'onsen/result.html', params)    