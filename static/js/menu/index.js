let vue_attr = {
	el: '#menu_main',
	data: {
		// 获取csrf验证的Key
		csrfmiddlewaretoken : $('#csrf_token').val(),
		// 菜品数据
		dishes_list : [],
		// 分类数据
		classification_list : [],
		// 用于显示详情或编辑的单个数据
		detail_data : {},
		// 用于保存上传图片对象
		detail_img : null,
		// 控制表格编辑的显示
		show_detail_box : false,
		// 详情的图片
		detail_fileList:[],
		// 详情上传显示
		uploadDisabled : true,
		// 表单提交方式
		ajax_type : 'post',
		// 分类窗口显示
		show_classification_box : false,
		// 分类数据
		classification_data : {},
		// 当前分页
		page : 1,
		// 分页总数
		page_total: 0,
		// 分页大小
		page_size: 10,
		// 分页页码大小
		page_sizes: [10, 30, 50, 100],
	},
	methods: {
		// 获取所有菜品
		get_dishes_list:function(){
			let vue = this;
			let page = vue.page
			let page_size = vue.page_size
			$.ajax({
				url : '/menu/dishes_page/?page='+page+'&&page_size='+page_size,
				type: 'get',
				success : function(res){
					if(res){
						vue.page_total = res.count
						vue.dishes_list = res.results
					}
				}
			});
		},
		// 获取所有菜品分类
		get_food_classification_list:function(){
			let vue = this;
			$.ajax({
				url : '/menu/food_classification/',
				type: 'get',
				success : function(res){
					if(res){
						vue.classification_list = res
					}
				}
			});
		},
		pageSizeChange:function(val){
			let vue = this;
			vue.page_size = val;
			vue.get_dishes_list();
		},
		pageCurrentChange:function(val){
			let vue = this;
			vue.page = val;
			vue.get_dishes_list();
		},
		// 上传按钮改变事件
		upload_change:function(file, fileList){
			let vue = this;
			if (file.size > 1024 * 100) {
				vue.$refs.upload.clearFiles();
				vue.uploadDisabled = false;
				vue.$message({
					message: "上传图片大小不能超过 100kb!",
					type: "error"
				});
			} else {
				vue.uploadDisabled = fileList.length >= 1;
				vue.detail_img = file.raw
			}

		},
		// 上传按钮删除事件
		upload_remove:function(file, fileList){
			let vue = this;
			vue.$refs.upload.clearFiles()
			vue.uploadDisabled = fileList.length >= 1;
			vue.detail_img = null
		},
		// 编辑表单提交
		detail_submit:function(){
			let vue = this;
			let formObj = vue.$refs['form'];
			let form = $('#upload_form')[0]
			var formData = new FormData(form)
			if(!vue.detail_img){
				formData.delete("img",vue.detail_img)
			}
			formData.set('classification',formObj.model.classification)
			formData.set('shelves_status',formObj.model.shelves_status)

			let id = vue.detail_data.id;
			let ajax_type = vue.ajax_type
			let url = '/menu/dishes/'

			if(ajax_type == 'put'){
				url = '/menu/dishes/'+id
			}
			$.ajax({
				url : url,
				type: ajax_type,
				headers: {'X-CSRFToken': vue.csrfmiddlewaretoken}, 
				processData: false,//重要
				contentType: false,//重要
				data: formData,
				success : function(res){
					vue.get_dishes_list()
					vue.show_detail_box = false;
				},
				error : function(res){
					console.log(res)
				}
			});
		},
		// 分类表单提交
		classification_submit:function(){
			let vue = this;
			let formData = vue.classification_data;
			$.ajax({
				url : '/menu/food_classification/',
				type: 'post',
				headers: {'X-CSRFToken': vue.csrfmiddlewaretoken}, 
				data: formData,
				success : function(res){
					vue.get_food_classification_list()
					vue.show_classification_box = false;
					vue.classification_data = {}
				},
				error : function(res){
					console.log(res)
				}
			});
		},
		// 新增菜品
		add_dishes:function(){
			let vue = this;
			vue.ajax_type = 'post'
			vue.detail_data = {};
			vue.detail_fileList = []
			vue.uploadDisabled = false;
			vue.show_detail_box = true;
		},
		// 表格编辑按钮事件
		tableEdit:function(data){
			let vue = this;
			vue.ajax_type = 'put'
			vue.detail_data = _.clone(data);
			vue.detail_fileList = [{name:'img',url:data.img}]
			vue.uploadDisabled = true;
			vue.show_detail_box = true;
		},
		// 表格删除按钮事件
		tableDelete:function(data){
			let vue  = this;
			let id = data.id;
			$.ajax({
				url : '/menu/dishes/'+id,
				type: 'delete',
				headers: {'X-CSRFToken': vue.csrfmiddlewaretoken}, 
				contentType: "application/json",
				success : function(res){
					/*let list = _.clone(vue.dishes_list)
					_.remove(list, function(n) {
						return n.id == id;
					});
					vue.dishes_list = list*/
					vue.get_dishes_list()
				},
				error : function(res){
					console.log(res)
				}
			});
		}
	},
	mounted: function (){
		let vue = this;
		vue.get_dishes_list();
		vue.get_food_classification_list();

	}
}

$(function(){ 
	let menu_vue = new Vue(vue_attr)
})