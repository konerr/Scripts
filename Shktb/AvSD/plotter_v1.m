clear all
format long e

home = '/home/local/UFAD/rahul.koneru/post_processing/force-model/10micro-All/' ;

dir_mic10 = 'MicroData/Data_For_Rahul/10/' ;
mic10_0 = load(strcat(home,dir_mic10,'Time_1.dat' ));
mic10_1 = load(strcat(home,dir_mic10,'Time_32.dat')) ;
mic10_2 = load(strcat(home,dir_mic10,'Time_62.dat')) ;
mic10_3 = load(strcat(home,dir_mic10,'Time_93.dat')) ;

dir_th = 'MicroData/Theory/' ;
th_10 = load(strcat(home,dir_th,'Area10.dat')) ;

dir_NF2way = 'NoFluc_2way/' ;
NF2way_t0 = load(strcat(home,dir_NF2way,'shktb.yzavg_0.00000E+00.dat')) ;
NF2way_t1 = load(strcat(home,dir_NF2way,'shktb.yzavg_4.03173E-07.dat')) ;
NF2way_t2 = load(strcat(home,dir_NF2way,'shktb.yzavg_8.04525E-07.dat')) ;
NF2way_t3 = load(strcat(home,dir_NF2way,'shktb.yzavg_1.20588E-06.dat')) ;
NF2way_t4 = load(strcat(home,dir_NF2way,'shktb.yzavg_1.40000E-06.dat')) ;

dir_nf1 = 'nf_1way/' ;
nf1_t0 = load(strcat(home,dir_nf1,'shktb.yzavg_0.00000E+00.dat')) ;
nf1_t1 = load(strcat(home,dir_nf1,'shktb.yzavg_3.99793E-07.dat')) ;
nf1_t2 = load(strcat(home,dir_nf1,'shktb.yzavg_7.99809E-07.dat')) ;
nf1_t3 = load(strcat(home,dir_nf1,'shktb.yzavg_1.20046E-06.dat')) ;
nf1_t4 = load(strcat(home,dir_nf1,'shktb.yzavg_1.40000E-06.dat')) ;

dir_sharp1 = 'sharpPhi_1way/' ;
sharp1_t0 = load(strcat(home,dir_sharp1,'shktb.yzavg_0.00000E+00.dat')) ;
sharp1_t1 = load(strcat(home,dir_sharp1,'shktb.yzavg_4.02147E-07.dat')) ;
sharp1_t2 = load(strcat(home,dir_sharp1,'shktb.yzavg_8.02005E-07.dat')) ;
sharp1_t3 = load(strcat(home,dir_sharp1,'shktb.yzavg_1.20471E-06.dat')) ;
sharp1_t4 = load(strcat(home,dir_sharp1,'shktb.yzavg_1.40000E-06.dat')) ;

dir_nqs = 'NoQS_2way/' ;
nqs_t0 = load(strcat(home,dir_nqs,'shktb.yzavg_0.00000E+00.dat')) ;
nqs_t1 = load(strcat(home,dir_nqs,'shktb.yzavg_4.03030E-07.dat')) ;
nqs_t2 = load(strcat(home,dir_nqs,'shktb.yzavg_8.04382E-07.dat')) ;
nqs_t3 = load(strcat(home,dir_nqs,'shktb.yzavg_1.20439E-06.dat')) ;
nqs_t4 = load(strcat(home,dir_nqs,'shktb.yzavg_1.40000E-06.dat')) ;

dir_fixPG_nqs = 'FixPG_NoQS_2way/' ;
fixPG_nqs_t0 = load(strcat(home,dir_fixPG_nqs,'shktb.yzavg_0.00000E+00.dat')) ;
fixPG_nqs_t1 = load(strcat(home,dir_fixPG_nqs,'shktb.yzavg_4.02913E-07.dat')) ;
fixPG_nqs_t2 = load(strcat(home,dir_fixPG_nqs,'shktb.yzavg_8.02781E-07.dat')) ;
fixPG_nqs_t3 = load(strcat(home,dir_fixPG_nqs,'shktb.yzavg_1.20518E-06.dat')) ;
fixPG_nqs_t4 = load(strcat(home,dir_fixPG_nqs,'shktb.yzavg_1.40000E-06.dat')) ;

dir_fixPG_nf2 = 'FixPG_NoFluc_2way/' ;
fixPG_nf2_t0 = load(strcat(home,dir_fixPG_nf2,'shktb.yzavg_0.00000E+00.dat')) ;
fixPG_nf2_t1 = load(strcat(home,dir_fixPG_nf2,'shktb.yzavg_4.02693E-07.dat')) ;
fixPG_nf2_t2 = load(strcat(home,dir_fixPG_nf2,'shktb.yzavg_8.03554E-07.dat')) ;
fixPG_nf2_t3 = load(strcat(home,dir_fixPG_nf2,'shktb.yzavg_1.20479E-06.dat')) ;
fixPG_nf2_t4 = load(strcat(home,dir_fixPG_nf2,'shktb.yzavg_1.40000E-06.dat')) ;

mic10_t = cat(3,mic10_0,mic10_1,mic10_2,mic10_3) ;

nf2way_t = cat(3,NF2way_t0,NF2way_t1,NF2way_t2,NF2way_t3,NF2way_t4) ;

nf1_t = cat(3,nf1_t0,nf1_t1,nf1_t2,nf1_t3,nf1_t4) ;
sharp1_t = cat(3,sharp1_t0,sharp1_t1,sharp1_t2,sharp1_t3,sharp1_t4) ;

nqs_t = cat(3,nqs_t0,nqs_t1,nqs_t2,nqs_t3,nqs_t4) ;

fixPG_nqs_t = cat(3,fixPG_nqs_t0,fixPG_nqs_t1,fixPG_nqs_t2,fixPG_nqs_t3,fixPG_nqs_t4) ;

fixPG_nf2_t = cat(3,fixPG_nf2_t0,fixPG_nf2_t1,fixPG_nf2_t2,fixPG_nf2_t3,fixPG_nf2_t4) ;

Ms = 3.0 ;
p = 101325 ;
rho = 1.2048 ;
gamma = 1.4 ;
us = Ms*sqrt(gamma*p/rho) ;
dp = 100E-6 ;
tau = dp/us ;

color_meso = {'r','g','b','k'} ;
color_micr = {'o-r','o-g','o-b','o-k'} ;
color_syms = {'sr','sg','sb','s-k'} ;

var = 2 ; % 2,3,6
micvar = 32 ; % 32,33,35
ymax = 2.5 ;

for i = 1:4
    x_nd = (nf2way_t(:,1,i)-0.001078)/dp ;
    p_nd = nf2way_t(:,3,i)/nf2way_t(1,3,i) ;

%     figure(1)
% %     plot(x_nd,p_nd,color_meso{i},'LineWidth',2)
%     plot(x_nd,twoway_t(:,var,i)/twoway_t(1,var,i),color_micr{i},'LineWidth',2)
% %     plot(x_nd,fluc10_t(:,3,i),color_meso{i},'LineWidth',2)
% %     plot(x_nd,qs_t(:,var,i)/qs_t(1,var,i),color_micr{i},'LineWidth',2)
%     
%     hold on
% %     plot(x_nd,twoway_t(:,3,i)/twoway_t(1,3,i),color_micr{i})
% %     plot(x_nd,vu_t(:,3,i)/vu_t(1,3,i),color_micr{i},'LineWidth',2)
%     plot(x_nd,nf2way_t(:,var,i)/nf2way_t(1,var,i),color_meso{i},'LineWidth',2)
%     
% %     lgd =  legend('1-Way','2-Way') ;
%     lgd =  legend('\phi^{''}=10%','\phi^{''}=0') ; 
%     lgd.Location = 'northeast' ;       
%     lgd.FontSize = 12 ;
%     legend('boxoff') 
%     
%     xlabel('x/d_p','FontSize',16,'FontWeight','bold')
%     ylabel('<p>','FontSize',16,'FontWeight','bold')
%     grid on
%     
%     ylim([0 ymax])
%     xlim([-5 15])    
end
%     print('mes_12_ux','-dpng','-r300')
%     print('mes_2fnf_rho','-dpng','-r300')

for i = 4:4
    figure(2)
%     plot(x_nd,p_nd,color_meso{i},'LineWidth',2)
%     plot(x_nd,qs_t(:,2,i)/qs_t(1,2,i)./(1-qs_t(:,9,i)),color_micr{i},'LineWidth',2)
    
    hold on

%     yyaxis left
%     plot(x_nd,twoway_t(:,3,i)/twoway_t(1,3,i),color_micr{i})
    plot(x_nd,nf2way_t(:,2,i)/nf2way_t(1,2,i)./(1-nf2way_t(:,9,i)),color_meso{i},'LineWidth',2)
%     plot(x_nd,nqs_t(:,2,i)/nqs_t(1,2,i)./(1-nqs_t(:,9,i)),color_micr{i},'LineWidth',2)
%     plot(x_nd,fixPG_nqs_t(:,2,i)/fixPG_nqs_t(1,2,i)./(1-fixPG_nqs_t(:,9,i)),color_syms{i},'LineWidth',2)
    plot(x_nd,fixPG_nf2_t(:,2,i)/fixPG_nf2_t(1,2,i)./(1-fixPG_nf2_t(:,9,i)),color_syms{i},'LineWidth',2)

%     plot(x_nd,nf1_t(:,2,i)/nf1_t(1,2,i)./(1-nf1_t(:,9,i)),color_micr{i},'LineWidth',2)
%     plot(x_nd,sharp1_t(:,2,i)/sharp1_t(1,2,i)./(1-sharp1_t(:,9,i)),color_meso{i},'LineWidth',2)
%     plot(th_10(:,1),th_10(:,3)/th_10(1,3),'r','LineWidth',2) 
    
    plot((mic10_t(:,1,i)/dp)+7.8,mic10_t(:,32,i),color_micr{i},'MarkerSize',8);

%     lgd =  legend('1-Way','2-Way','Micro') ;
    lgd =  legend('2-Way','Micro') ;    
    lgd.Location = 'northeast' ;       
    lgd.FontSize = 12 ;
    legend('boxoff')    

    xlabel('x/d_p','FontSize',16,'FontWeight','bold')
    ylabel('<\rho>','FontSize',16,'FontWeight','bold')

    grid on
%     grid minor
    ylim([0 1.8])
    xlim([-5 15])      
end
%     print('micr_nf2_rho','-dpng','-r300')
%     print('nf12_rho','-dpng','-r300')

for i = 4:4
    figure(3)
%     plot(x_nd,p_nd,color_meso{i},'LineWidth',2)
%     plot(x_nd,qs_t(:,3,i)/qs_t(1,3,i),color_micr{i},'LineWidth',2)
    
    hold on
%     plot(x_nd,twoway_t(:,3,i)/twoway_t(1,3,i),color_micr{i})
    plot(x_nd,nf2way_t(:,3,i)/nf2way_t(1,3,i),color_meso{i},'LineWidth',2)
%     plot(x_nd,nqs_t(:,3,i)/nqs_t(1,3,i),color_micr{i},'LineWidth',2)
%     plot(x_nd,fixPG_nqs_t(:,3,i)/fixPG_nqs_t(1,3,i),color_syms{i},'LineWidth',2)
    plot(x_nd,fixPG_nf2_t(:,3,i)/fixPG_nf2_t(1,3,i),color_syms{i},'LineWidth',2)

%     plot(x_nd,nf1_t(:,3,i)/nf1_t(1,3,i),color_micr{i},'LineWidth',2)
%     plot(x_nd,sharp1_t(:,3,i)/sharp1_t(1,3,i),color_meso{i},'LineWidth',2)    
%     plot(th_10(:,1),th_10(:,2)/th_10(1,2),'r','LineWidth',2)
%     hold on
    plot((mic10_t(:,1,i)/dp)+7.8,mic10_t(:,33,i),color_micr{i},'MarkerSize',8);

%     lgd =  legend('1-Way','2-Way','Micro') ;
    lgd =  legend('2-Way','Micro') ;
    lgd.Location = 'northeast' ;       
    lgd.FontSize = 12 ;
    legend('boxoff')    

    xlabel('x/d_p','FontSize',16,'FontWeight','bold')
    ylabel('<p>','FontSize',16,'FontWeight','bold')

    grid on
%     grid minor
    ylim([0 2.5])
    xlim([-5 15])      
end
%     print('micr_nf2_p','-dpng','-r300')
%     print('nf12_p','-dpng','-r300')


for i = 4:4
    figure(4)
%     plot(x_nd,p_nd,color_meso{i},'LineWidth',2)
%     plot(x_nd,qs_t(:,6,i)/qs_t(1,6,i),color_micr{i},'LineWidth',2)
    
    hold on
%     plot(x_nd,twoway_t(:,3,i)/twoway_t(1,3,i),color_micr{i})
    plot(x_nd,nf2way_t(:,6,i)/nf2way_t(1,6,i),color_meso{i},'LineWidth',2)
%     plot(x_nd,nqs_t(:,6,i)/nqs_t(1,6,i),color_micr{i},'LineWidth',2)
%     plot(x_nd,fixPG_nqs_t(:,6,i)/fixPG_nqs_t(1,6,i),color_syms{i},'LineWidth',2)
    plot(x_nd,fixPG_nf2_t(:,6,i)/fixPG_nf2_t(1,6,i),color_syms{i},'LineWidth',2)
    
%     plot(x_nd,nf1_t(:,6,i)/nf1_t(1,6,i),color_micr{i},'LineWidth',2)
%     plot(x_nd,sharp1_t(:,6,i)/sharp1_t(1,6,i),color_meso{i},'LineWidth',2)    
%     plot(th_10(:,1),th_10(:,4)/th_10(1,4),'r','LineWidth',2) 

%     hold on
    plot((mic10_t(:,1,i)/dp)+7.8,mic10_t(:,35,i),color_micr{i},'MarkerSize',8);

%     lgd =  legend('1-Way','2-Way','Micro') ;
    lgd =  legend('2-Way','Micro') ;
    lgd.Location = 'northeast' ;       
    lgd.FontSize = 12 ;
    legend('boxoff')    

    xlabel('x/d_p','FontSize',16,'FontWeight','bold')
    ylabel('<u_x>','FontSize',16,'FontWeight','bold')

    grid on
%     grid minor
    ylim([0 1.2])
    xlim([-5 15])      
end
%     print('micr_nf2_ux','-dpng','-r300')
%     print('nf12_ux','-dpng','-r300')

%%
figure(5)

plot(th_10(:,1),th_10(:,2)/th_10(1,2),'k','LineWidth',2) 
hold on
% plot(x_nd,qs_t(:,3,4)/qs_t(1,3,4),'r','LineWidth',2)
plot(x_nd,nf1_t(:,3,4)/nf1_t(1,3,4),'r','LineWidth',2)
hold on
% for i=4:4
%     plot(x_nd,tru_t(:,3,i)/tru_t(1,3,i),color_meso{i},'LineWidth',2)
% %     plot(qs_t(:,1,i),qs_t(:,3,i)/qs_t(1,3,i),color_meso{i},'LineWidth',2)
%     hold on
% end
xlabel('x/d_p','FontSize',16,'FontWeight','bold')
ylabel('<p>','FontSize',16,'FontWeight','bold')

lgd =  legend('Theory','1-Way') ;
lgd.Location = 'northeast' ;       
lgd.FontSize = 12 ;
legend('boxoff')  
xlim([-5 15])
% print('th_nf1_p','-dpng','-r300')

figure(6)

plot(th_10(:,1),th_10(:,3)/th_10(1,3),'k','LineWidth',2) 
hold on
% plot(x_nd,qs_t(:,2,4)/qs_t(1,2,4)./(1-qs_t(:,9,4)),'r','LineWidth',2)
plot(x_nd,nf1_t(:,2,4)/nf1_t(1,2,4)./(1-nf1_t(:,9,4)),'r','LineWidth',2)

% hold on
% plot(x_nd,qs_t(:,2,4)/qs_t(1,2,4),'b','LineWidth',2)
xlabel('x/d_p','FontSize',16,'FontWeight','bold')
ylabel('<\rho>','FontSize',16,'FontWeight','bold')

lgd =  legend('Theory','1-Way') ;
lgd.Location = 'northeast' ;       
lgd.FontSize = 12 ;
legend('boxoff')    
xlim([-5 15])
% print('th_nf1_rho','-dpng','-r300')

figure(7)

plot(th_10(:,1),th_10(:,4)/th_10(1,4),'k','LineWidth',2) 
hold on
% plot(x_nd,qs_t(:,6,4)/qs_t(1,6,4),'r','LineWidth',2)
plot(x_nd,nf1_t(:,5,4)/nf1_t(1,5,4),'r','LineWidth',2)

xlabel('x/d_p','FontSize',16,'FontWeight','bold')
ylabel('<u_x>','FontSize',16,'FontWeight','bold')

lgd =  legend('Theory','1-Way') ;
lgd.Location = 'northeast' ;       
lgd.FontSize = 12 ;
legend('boxoff')    
xlim([-5 15])
% print('th_nf1_ux','-dpng','-r300')

%%
% np = 25 ;
% nd = 10 ;
% k=0:np ;
% nv = 1:nd ;
% for i = 1:length(nv)
%     prob=(nv(i).^k).*exp(-nv(i))./factorial(k) ;
%     plot(k,prob,'LineWidth',2)
%     hold on
%     
%     xlabel('k','FontWeight','bold')
%     ylabel('P_k','FontWeight','bold')
%     x = [0.35 0.5];
%     y = [0.6 0.5];
%     annotation('textarrow',x,y,'String','N_v \epsilon [1,10] ')
% end
%     print('pdf','-dpng','-r300')

