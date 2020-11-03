
function test01() {
    var es=table.column().header()
    alert();



}
function reloadajax() {
    table.ajax.reload();
    alert('刷新成功')

}
function addrow() {
    var selecttype=table.select.items();
    if (selecttype=='row'){var es=table.rows({ selected: true }).data(d);alert('item类型row')}
    else if(selecttype=='column'){var es=table.columns({ selected: true }).data();alert('item类型col')}
    else if(selecttype=='cell'){var es=table.cells({ selected: true }).data();alert('item类型cell')}
    else {return alert('item类型错误')}
    alert('test')
}
function editrow() {
    var selecttype=table.select.items();



    if (selecttype=='row'){var es=table.rows({ selected: true }).data();for (i=0;i<es.length;i++){alert(es[i])}}
    else if(selecttype=='column'){var es=table.columns({ selected: true }).data();for (i=0;i<es.length;i++){alert(es[i])}}
    else if(selecttype=='cell'){var es=table.cells({ selected: true }).data();for (i=0;i<es.length;i++){alert(es[i])}}

    else {return alert('item类型错误')}


}
function delrow() {
    var selecttype=exm.select.items();
    if (selecttype=='row'){var es=exm.rows({ selected: true }).data();alert(exm.row({ selected: true }).index())}
    else if(selecttype=='column'){var es=table.columns({ selected: true }).data();alert('item类型col')}
    else if(selecttype=='cell'){var es=table.cells({ selected: true }).data();alert(table.cell({ selected: true }).index().row)}
    else {return alert('item类型错误')}
    alert('test')
}
