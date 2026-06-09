import numpy as np
import matplotlib.pyplot as plt

class DissConnecTed_FPU:
    def __init__(self, base_freq=1e9):
        """
        DissConnecTed Fourier Processing Unit (FPU) Core Simulator.
        Mimari tamamen analog dalga etkileşimleri üzerine kuruludur.
        """
        self.base_freq = base_freq # 1 GHz Taşıyıcı Frekans
        
    def simulate_ai_matrix_multiply(self, inputs, phases):
        """
        1. MOD: Yapay Zeka Matris Çarpım Çekirdeği (O(1) Zamanda Girişim)
        """
        t = np.linspace(0, 2e-9, 1000) # 2 nanosaniyelik zaman penceresi
        individual_waves = []
        result_wave = np.zeros_like(t)
        
        for amp, phi in zip(inputs, phases):
            wave = amp * np.sin(2 * np.pi * self.base_freq * t + phi)
            individual_waves.append(wave)
            result_wave += wave # Pasif Çekirdekte Kirchhoff Toplamı
            
        return t, individual_waves, result_wave

    def simulate_quantum_emulation(self, state_a_phase, state_b_phase):
        """
        2. MOD: Klasik Donanımda Kuantum Durum/Dolanıklık Simülasyonu
        """
        t = np.linspace(0, 2e-9, 1000)
        wave_a = 1.0 * np.sin(2 * np.pi * self.base_freq * t + state_a_phase)
        wave_b = 1.0 * np.sin(2 * np.pi * self.base_freq * t + state_b_phase)
        
        # Süperpozisyon (Üst üste binme)
        superposition_wave = (wave_a + wave_b) / np.sqrt(2)
        
        return t, wave_a, wave_b, superposition_wave

# --- GÖRSELLEŞTİRME VE ÇALIŞTIRMA KATMANI ---
if __name__ == "__main__":
    try:
        fpu = DissConnecTed_FPU(base_freq=1e9)
        
        # -----------------------------------------------------------------
        # GRAFİK 1: YAPAY ZEKA MATRİS ÇARPIM SİMÜLASYONU
        # -----------------------------------------------------------------
        ai_inputs = [1.5, 0.7, 1.2, 0.4]       # Vektör girdileri (Genlik)
        ai_weights = [0.0, np.pi/3, np.pi/2, np.pi] # Matris ağırlıkları (Faz)
        
        t_ai, ind_waves, res_wave = fpu.simulate_ai_matrix_multiply(ai_inputs, ai_weights)
        
        # Manuel Siberpunk Karanlık Arka Plan Ayarı (Hata ihtimalini sıfırlar)
        fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
        fig1.patch.set_facecolor('#121212')
        ax1.set_facecolor('#1e1e1e')
        ax2.set_facecolor('#1e1e1e')
        
        fig1.suptitle('⚡ FPU AI Matrix Core (Designed by DissConnecTed)', fontsize=14, color='#00ffcc', fontweight='bold')
        
        colors = ['#ff0055', '#00ff55', '#0055ff', '#ffaa00']
        for i, w in enumerate(ind_waves):
            ax1.plot(t_ai * 1e9, w, color=colors[i], alpha=0.7, label=f'Kanal {i+1} (A={ai_inputs[i]}, \u03a6={ai_weights[i]:.2f} rad)')
        ax1.set_title('Giriş Katmanı: DDS Üreteçlerinden Çıkan Saf Sinüsler', color='#abcdef', fontsize=10)
        ax1.set_ylabel('Voltaj (V)', color='#abcdef')
        ax1.tick_params(colors='white')
        ax1.grid(True, linestyle='--', alpha=0.1, color='white')
        ax1.legend(loc='upper right', fontsize=8, facecolor='#121212', labelcolor='white')
        
        ax2.plot(t_ai * 1e9, res_wave, color='#00ffcc', linewidth=2.5, label='Pasif Çıkış Süper Dalgası (O(1) Çarpım Sonucu)')
        max_idx = np.argmax(np.abs(res_wave))
        ax2.scatter(t_ai[max_idx] * 1e9, res_wave[max_idx], color='white', s=40, zorder=5)
        ax2.annotate(f' ADC Örnekleme: {res_wave[max_idx]:.3f}V', xy=(t_ai[max_idx] * 1e9, res_wave[max_idx]), color='white')
        ax2.set_title('Hesaplama Katmanı: Çekirdekte Oluşan Fiziksel Girişim', color='#abcdef', fontsize=10)
        ax2.set_xlabel('Zaman (Nanosaniye)', color='#abcdef')
        ax2.set_ylabel('Voltaj (V)', color='#abcdef')
        ax2.tick_params(colors='white')
        ax2.grid(True, linestyle='--', alpha=0.1, color='white')
        ax2.legend(loc='upper right', fontsize=9, facecolor='#121212', labelcolor='white')
        
        plt.tight_layout()
        plt.savefig('fpu_ai_core.png', dpi=300, facecolor=fig1.get_facecolor(), edgecolor='none')
        
        # -----------------------------------------------------------------
        # GRAFİK 2: KUANTUM DOLANIKLIĞI / SÜPERPOZİSYON EMÜLASYONU
        # -----------------------------------------------------------------
        t_q, w_a, w_b, s_wave = fpu.simulate_quantum_emulation(state_a_phase=0, state_b_phase=np.pi/1.2)
        
        fig2, ax = plt.subplots(figsize=(11, 5))
        fig2.patch.set_facecolor('#121212')
        ax.set_facecolor('#1e1e1e')
        fig2.suptitle('\u269b\ufe0f FPU Quantum Emulation Mode (Designed by DissConnecTed)', fontsize=14, color='#ff00ff', fontweight='bold')
        
        ax.plot(t_q * 1e9, w_a, '--', color='#0055ff', alpha=0.6, label='Kübit Durum A (Faz: 0)')
        ax.plot(t_q * 1e9, w_b, '--', color='#ffaa00', alpha=0.6, label='Kübit Durum B (Faz: 5\u03c0/6)')
        ax.plot(t_q * 1e9, s_wave, color='#ff00ff', linewidth=3, label='Süperpozisyon Genlik Dalgası')
        
        ax.set_title('Dalga Mekaniğiyle Kuantum Durum İzleme ve Olasılık Girişimi', color='#abcdef', fontsize=10)
        ax.set_xlabel('Zaman (Nanosaniye)', color='#abcdef')
        ax.set_ylabel('Genlik / Olasılık Voltajı', color='#abcdef')
        ax.tick_params(colors='white')
        ax.grid(True, linestyle='--', alpha=0.1, color='white')
        ax.legend(loc='upper right', facecolor='#121212', labelcolor='white')
        
        plt.tight_layout()
        plt.savefig('fpu_quantum_core.png', dpi=300, facecolor=fig2.get_facecolor(), edgecolor='none')
        
        print("\n[DissConnecTed FPU Pipeline] Simülasyon başarıyla tamamlandı!")
        print("-> Yapay zeka matris grafiği kaydedildi: 'fpu_ai_core.png'")
        print("-> Kuantum emülasyon grafiği kaydedildi: 'fpu_quantum_core.png'")
        
        print("\nGrafikler ekrana getiriliyor...")
        plt.show()

    except Exception as e:
        print(f"\n[HATA OLUŞTU]: {e}")
    
    # Terminalin aniden kapanmasını engelleyen can simidi:
    input("\nProgramın kapanmasını engellemek için ENTER'a basın...")