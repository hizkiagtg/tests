$(document).ready(() => {
    $.get('/tukarpoin/json', (voucher) => {
        $('#vouchers-section').append(`
            <h1 id="num-of-vouchers">
                ${voucher.length} voucher
            </h1>
        `)
        tasks.forEach((voucher) => {
            $('#vouchers-section').append(`
                <div id="task-${voucher.pk}" data-aos="flip-up" class="mt-2 py-4 px-6 bg-gray-100 items-center justify-between rounded-md flex transition ease-in-out hover:scale-105 hover:bg-gray-200">
                    <div class="flex items-center">
                        <div class="pl-6">
                            <h2 class="font-bold">
                            ${voucher.fields.title}
                            </h2>
                            <h3>
                                ${voucher.fields.voucherbank}
                            </h3>
                            <p class="text-gray-500">Province available: 
                            ${voucher.fields.area_required}
                            </p>
                            <p class="text-blue-600">Expired date: 
                            ${voucher.fields.expireddate}
                            </p>
                            <p class="text-gray-500">
                            ${voucher.fields.voucherbody}
                            </p>
                        </div>
                    </div>
                    <button onclick="redeemcheck()" id="redeemvoucher" class="text-red-600 p-2 rounded-md transition ease-in-out hover:scale-110">Redeem</button>
                </div>
            `)
      })
      
    })

    $.get('/tukarpoin/json', (voucher) => {
        $('#myvouchers-section').append(`
            <h1 id="num-of-vouchers">
                ${voucher.length} voucher
            </h1>
        `)
        tasks.forEach((voucher) => {
            $('#myvouchers-section').append(`
                <div id="task-${voucher.pk}" data-aos="flip-up" class="mt-2 py-4 px-6 bg-gray-100 items-center justify-between rounded-md flex transition ease-in-out hover:scale-105 hover:bg-gray-200">
                    <div class="flex items-center">
                        <div class="pl-6">
                            <h2 class="font-bold">
                            ${voucher.fields.title}
                            </h2>
                            <h3>
                                ${voucher.fields.voucherbank}
                            </h3>
                            <p class="text-gray-500">Province available: 
                            ${voucher.fields.area_required}
                            </p>
                            <p class="text-blue-600">Expired date: 
                            ${voucher.fields.expireddate}
                            </p>
                            <p class="text-gray-500">
                            ${voucher.fields.voucherbody}
                            </p>
                        </div>
                    </div>
                    <button onclick="redeemcheck() id="redeemvoucher" class="text-red-600 p-2 rounded-md transition ease-in-out hover:scale-110">Redeem</button>
                </div>
            `)
      })
      
    })
  
    
  
    $('#new-voucher-form').submit((e) => {
      e.preventDefault()
      $.ajax({
        url: '/tukarpoin/added/',
        type: 'POST',
        credentials: 'include',
        dataType: 'json',
        data: $('#new-voucher-form').serialize(),
        success: (voucher) => {
            $.get('/tukarpoin/json', (voucher) => {
                $('#vouchers-section').append(`
                  <h1 id="num-of-vouchers">
                    ${voucher.length} voucher
                  </h1>
                `)
                tasks.forEach((voucher) => {
                  $('#vouchers-section').append(`
                    <div id="task-${voucher.pk}" data-aos="flip-up" class="mt-2 py-4 px-6 bg-gray-100 items-center justify-between rounded-md flex transition ease-in-out hover:scale-105 hover:bg-gray-200">
                      <div class="flex items-center">
                        <div class="pl-6">
                          <h2 class="font-bold">
                            ${voucher.fields.title}
                          </h2>
                          <h3>
                              ${voucher.fields.voucherbank}
                          </h3>
                          <p class="text-gray-500">Province available: 
                            ${voucher.fields.area_required}
                          </p>
                          <p class="text-blue-600">Expired date: 
                            ${voucher.fields.expireddate}
                          </p>
                          <p class="text-gray-500">
                            ${voucher.fields.voucherbody}
                          </p>
                        </div>
                      </div>
                      <button id="redeemvoucher" class="text-red-600 p-2 rounded-md transition ease-in-out hover:scale-110">
                        Redeem
                      </button>
                    </div>
                  `)
                  $(`#redeemvoucher-${voucher.pk}`).click(() => {
                    console.log("DELETE")
                    $.ajax({
                      url: `/todolist/delete/${task.pk}`,
                      type: 'GET',
                      credentials: 'include',
                      success: () => $(`#task-${task.pk}`).remove()
                    })
                  })
                })
                
              })
        }
      })
    })
})

function redeemcheck(vouchers) {
    if (user_poin<vouchers.requiredpoin){
        alert("Donate more to gain more points!")
        return false
    }
    if (vouchers.available_voucher<0){
        alert("Please choose another voucher, the voucher currently out of stock!")
        return false
    }
    alert("Succes! Check your vouchers!")
    return true
}