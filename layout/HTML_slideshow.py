#slideshow_with_button
slideshow_carousel = \
{'div':{'id':'myCarousel', 'class':'carousel slide' , 'data-ride':'carousel'} , 'content':{
	1:{'ol':{'class':'carousel-indicators'} , 'content':{
      		1:{'li':{'data-target':'#myCarousel' , 'data-slide-to':""} , 'content':''}}},
	2:{'div':{'class':'carousel-inner'} , 'content':{
		1:{'div':{'class':'item'} , 'content':{
        		1:{'img':{'src':'', 'width':'100%'} , 'content':''},
			2:{'div':{'class':'carousel-caption'} , 'content':{
        				1:{'h3':{} , 'content':''}}}}}}},
	3:{'div':{} , 'content':{
	   	1:{'a':{'class':'left carousel-control' , 'href':'#myCarousel' ,'data-slide':'prev'} , 'content':{
			1:{ 'span':{'class':'glyphicon glyphicon-chevron-left'} , 'content':''},	
			2:{ 'span':{'class':'sr-only'} , 'content':'Previous'}}},
		2:{'a':{'class':'right carousel-control' , 'href':'#myCarousel' ,'data-slide':'next'} , 'content':{	
			1:{ 'span':{'class':'glyphicon glyphicon-chevron-right'} , 'content':''},
			2:{ 'span':{'class':'sr-only'} , 'content':'Next'}}}}}}}

#slideshow_auto_scroll
