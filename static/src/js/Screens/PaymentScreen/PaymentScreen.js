odoo.define('aspl_pos_order_sync.PaymentScreenInherit', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const { useRef, useState } = owl.hooks;

    //const PaymentScreenInherit = (PaymentScreen) =>
    //     class extends PaymentScreen {
    //         constructor(){
    //             super(...arguments);
    //         }

    //         async validateOrder(isForceValidate) {
    //             var payment_screen = super.validateOrder(isForceValidate);
    //             if(this.props.order_id){
    //                 var orders_list = this.env.pos.db.get_draft_orders_list();
    //                 orders_list = _.without(orders_list, _.findWhere(orders_list, { id: this.props.order_id }));
    //                 this.env.pos.db.add_draft_orders(orders_list);
    //                 this.trigger('reload-order-count',{ orders_count:orders_list.length});
    //             }
    //             return payment_screen;
    //         }
    //     }

    // Registries.Component.extend(PaymentScreen, PaymentScreenInherit);

    // return PaymentScreenInherit;


    const CustomPaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
        async validateOrder(isForceValidate) {
            // Llamada a la función original para mantener la funcionalidad base
            const isValid = await super.validateOrder(isForceValidate);

            // Asegurándose de que se respetan las validaciones específicas de boletas del módulo 10N CL
            if (this.env.pos.config.module_l10n_cl && this.currentOrder.es_boleta()) {
                // Aquí puedes agregar las validaciones o lógicas específicas requeridas por el módulo 10N CL
                // Por ejemplo, verificar si todos los datos necesarios para la boleta están presentes

                if (!this.currentOrder.client || !this.currentOrder.client.document_number) {
                    this.showPopup('ErrorPopup', {
                        title: "Datos de Cliente Incompletos",
                        body: "El Cliente seleccionado no tiene RUT, por favor verifique"
                    });
                    return false;
                }
            }

            return isValid;
            }
        };

        Registries.Component.extend(PaymentScreen, CustomPaymentScreen);

         return CustomPaymentScreen;});